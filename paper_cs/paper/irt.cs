/*
 * 由SharpDevelop创建。
 * 用户： pfermat
 * 日期: 2017/12/14
 * 时间: 10:53
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;
using System.Collections.Generic;

public struct betaParam
{
	private double _2j;
	private double[] _delta_j;
	
	public betaParam( double beta_2j, double[] beta_delta_j )
	{
		_2j = beta_2j;
		_delta_j = new double[beta_delta_j.Length];
		for ( int i = 0; i < _delta_j.Length; i++ )
		{
			_delta_j[i] = beta_delta_j[i];
		}
	}
	
	public betaParam( double[] beta_data )
	{
		_2j = beta_data[0];
		_delta_j = new double[beta_data.Length - 1];
		for ( int i = 0; i < _delta_j.Length; i++ )
		{
			_delta_j[i] = beta_data[i + 1];
		}
	}
	
	/// <summary>
	/// 获取beta_2j的值
	/// </summary>
	/// <returns></returns>
	public double beta_2j( )
	{
		return _2j;
	}
	
	/// <summary>
	/// 直接返回beta_delta_j数组
	/// </summary>
	/// <remarks>下标从0开始</remarks>
	/// <returns></returns>
	public double[] beta_delta_j( )
	{
		return _delta_j;
	}
	
	/// <summary>
	/// 返回指定index的beta_delta_j
	/// </summary>
	/// <param name="index">下标</param>
	/// <remarks>下标从2开始</remarks>
	/// <returns></returns>
	public double beta_delta_j( int index )
	{
		if ( index == 0 || index == 1 )
		{
			return 0.0;
		}
		else
		{
			return _delta_j[index - 2];
		}
	}
	
	/// <summary>
	/// 返回所有beta参数
	/// </summary>
	/// <param name="type">1 下标1为0；2 下标1为beta_2j</param>
	/// <remarks>下标0无用，下标1为0.0，下标从2开始为beta_delta_j</remarks>
	/// <returns></returns>
	public double[] beta_data( int type = 1)
	{
		List<double> tmp = new List<double>();
		tmp.Add(0.0);
		if ( type == 1)
		{
			tmp.Add(0.0);
		}
		else
		{
			tmp.Add(_2j);
		}
		
		for ( int i = 0; i < _delta_j.Length; i++ )
		{
			tmp.Add(_delta_j[i]);
		}
		
		return tmp.ToArray();
	}
}

public struct Item
{
	public int Index;
	public int Kj;
	public betaParam Betas;
	public double[] SumBeta;

	public Item( int index, int kj, double[] beta_data )
	{
		Index = index;
		Kj = kj;
		Betas = new betaParam(beta_data);
		SumBeta = new double[Betas.beta_data().Length + 1];
		
		for ( int i = 1; i < Betas.beta_data().Length + 1; i++ )
		{
			SumBeta[i] = sum_beta_delta(i - 1);
		}
	}
	
	public Item( int index, int kj, betaParam beta_data )
	{
		Index = index;
		Kj = kj;
		Betas = beta_data;
		SumBeta = new double[Betas.beta_data().Length + 1];
		
		for ( int i = 1; i < Betas.beta_data().Length + 1; i++ )
		{
			SumBeta[i] = sum_beta_delta(i - 1);
		}
	}
	
	private double sum_beta_delta( int m )
	{
		double sum = 0.0;
		for ( int i = 1; i <= m; i++ )
		{
			sum += Betas.beta_data()[i];
		}
		
		return sum;
	}
	
	private double denominator( int m, double theta )
	{
		return Math.Exp( (m - 1) * Betas.beta_2j() * theta - SumBeta[m] );
	}
	
	private double numerator( int k, double theta )
	{
		return Math.Exp( (k - 1) * Betas.beta_2j() * theta - SumBeta[k] );
	}
	
	private double sum_denominator( int K, double theta )
	{
		double sum = 0.0;
		for ( int i = 1; i < K + 1; i++ )
		{
			sum += denominator(i, theta);
		}
		
		return sum;
	}
	
	public double P_ijk( int k, double theta )
	{
		double numer = numerator(k, theta);
		double denom = sum_denominator(Kj, theta);
		
		return numer / denom;
	}
	
	private double[] pk( double theta )
	{
		List<double> p = new List<double>();
		p.Add(0.0);
		
		for ( int i = 1; i < Kj + 1; i++ )
		{
			p[i] = numerator(i, theta) / sum_denominator(Kj, theta);
		}
		
		return p.ToArray();
	}
	
	public double EX( double theta )
	{
		double[] p = pk(theta);
		double sum = 0.0;
		
		for ( int i = 1; i < p.Length; i++ )
		{
			sum += (i - 1) * p[i];
		}
		
		return sum;
	}
}

public static class irt
{
	public static bool sig_delta( int X_ij, int k )
	{
		if ( X_ij == k )
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	
	public static double logP( int N, int J, int[] KJ, int[,] X_ij, double[] thetas, betaParam[] betas )
	{
		double sum = 0.0;
		for ( int i = 0; i < N; i++ )
		{
			for ( int j = 0; j < J; j++ )
			{
				Item tmp = new Item(j, KJ[j], betas[j]);
				for ( int k = 0; k < KJ[j]; k++ )
				{
					if ( sig_delta(X_ij[i,j], k) )
					{
						sum += tmp.P_ijk(k + 1, thetas[i]);
					}
				}
			}
		}
		
		return sum;
	}
}