/*
 * 由SharpDevelop创建。
 * 用户： pfermat
 * 日期: 2017/12/14
 * 时间: 12:41
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;
using System.Collections.Generic;
using System.Linq;

public static class Var
{
	public static double PM = 0.05;
	public static double PC = 0.8;
	public static int POPU = 100;
	public static double r = 0.2;
	public static int GENE = 50;
	public static int tour = 2;
	public static double max_theta = 4.0;
	public static double max_beta = 20.0;
	public static double max_dis = 1.0;
}

public class Chrom : IComparable<Chrom>
{
	private ThreadSafeRandom safeRandom = new ThreadSafeRandom();
	public int N;
	public int[] KJ;
	public double[] Thetas;
	private double[] Betas;
	public betaParam[] BetaParams;
	private int[,] X_ij;
	
	public Chrom( int n, int[] kj, int[,] xij )
	{
		X_ij = xij;
		N = n;
		KJ = new int[kj.Length];
		for ( int i = 0; i < KJ.Length; i++ )
		{
			KJ[i] = kj[i];
			//count += KJ[i];
		}
		
		Thetas = new double[N];
		for ( int i = 0; i < Thetas.Length; i++ )
		{
			Thetas[i] = Signal() * Var.max_theta * safeRandom.NextDouble();
		}
		
		List<double> data = new List<double>();
		foreach ( var k in KJ )
		{
			data.Add( Signal() * Var.max_dis * safeRandom.NextDouble() );
			for ( int i = 1; i < k; i++ )
			{
				data.Add( Signal() * Var.max_beta * safeRandom.NextDouble() );
			}
		}
		Betas = data.ToArray();
		
		BetaParams = TransBeta();
	}
	
	private betaParam[] TransBeta( )
	{
		List<betaParam> data = new List<betaParam>();
		int index = 0;
		
		foreach( var k in KJ )
		{
			List<double> tmp = new List<double>();
			
			tmp.Add(Betas[index++]);
			for ( int i = 1; i < k; i++ )
			{
				tmp.Add(Betas[index++]);
			}
			
			data.Add(new betaParam(tmp.ToArray()));
		}
		
		return data.ToArray();
	}
	
	public double GetTheta( int index )
	{
		return Thetas[index - 1];
	}
	
	public void SetTheta( int index, double theta )
	{
		Thetas[index - 1] = theta;
	}
	
	private static int Signal( )
	{
		ThreadSafeRandom safe = new ThreadSafeRandom();
		
		return safe.Next(0, 2) == 0 ? 1 : -1;
	}
	
	public static Tuple<Chrom, Chrom> Cross( Chrom g1, Chrom g2 )
	{
		Chrom new_g1 = new Chrom(g1.N, g1.KJ, g1.X_ij);
		Chrom new_g2 = new Chrom(g1.N, g1.KJ, g1.X_ij);
		
		for ( int i = 0; i < g1.Thetas.Length; i++ )
		{
			new_g1.Thetas[i] = Var.r * g1.Thetas[i] + ( 1 - Var.r ) * g2.Thetas[i];
			new_g2.Thetas[i] = ( 1 - Var.r ) * g1.Thetas[i] + Var.r * g2.Thetas[i];
		}
		
		for ( int i = 0; i < g1.Betas.Length; i++ )
		{
			new_g1.Betas[i] = Var.r * g1.Betas[i] + ( 1 - Var.r ) * g2.Betas[i];
			new_g2.Betas[i] = ( 1 - Var.r ) * g1.Betas[i] + Var.r * g2.Betas[i];
		}
		
		new_g1.BetaParams = new_g1.TransBeta();
		new_g2.BetaParams = new_g2.TransBeta();
		
		return new Tuple<Chrom, Chrom>( new_g1, new_g2 );
	}
	
	public static Tuple<Chrom, Chrom> Select( Chrom[] population )
	{
		int count = population.Length;
		int[] competitors_1 = RandomSample.Sample(Var.tour, 0, count);
		int[] competitors_2 = RandomSample.Sample(Var.tour, 0, count);
		
		Chrom father = Max(competitors_1, population);
		Chrom mother = Max(competitors_2, population);
		
		return new Tuple<Chrom, Chrom>(father, mother);
	}
	
	public void Mutation( )
	{
		if ( Signal() == 1 )
		{
			int len = Thetas.Length;
			int index = safeRandom.Next(0, len);
			Thetas[index] = Signal() * Var.max_theta * safeRandom.NextDouble();
		}
		else
		{
			;
		}
	}
	
	public double fitness( )
	{
		return irt.logP( N, KJ.Length, KJ, X_ij, Thetas, BetaParams );
	}
	
	public int CompareTo( Chrom other )
	{
		return this.fitness().CompareTo(other.fitness());
	}
	
	private static Chrom Max( int[] indices, Chrom[] chroms )
	{
		Dictionary<int, double> data = new Dictionary<int, double>();
		for ( int i = 0; i < indices.Length; i++ )
		{
			data[indices[i]] = chroms[i].fitness();
		}
		
		int maxkey = data.Keys.Select(x => new { x, y = data[x] }).OrderBy(x => x.y).Last().x;
		return chroms[maxkey];
	}
	
	public static Chrom Max( Chrom[] chroms )
	{
		Dictionary<int, double> data = new Dictionary<int, double>();
		for ( int i = 0; i < chroms.Length; i++ )
		{
			data[i] = chroms[i].fitness();
		}
		
		int maxkey = data.Keys.Select(x => new { x, y = data[x] }).OrderBy(x => x.y).Last().x;
		return chroms[maxkey];
	}
}