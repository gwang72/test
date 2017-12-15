/*
 * 由SharpDevelop创建。
 * 用户： pfermat
 * 日期: 2017/12/14
 * 时间: 10:52
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */
using System;
using System.Collections.Generic;

namespace paper
{
	class Program
	{
		public static void Main(string[] args)
		{
			//Console.WriteLine("Hello World!");
			
//			Chrom[] test = new Chrom[10];
//			
//			for ( int i = 0; i < 10; i++ )
//			{
//				test[i] = new Chrom(Data.score.GetLength(0), Data.max_score, Data.score);
//			}
//			
//			for ( int i = 0; i < 50; i++ )
//			{
//				for ( int index = 0; index < 10; index++ )
//				{
//					Console.WriteLine("{0}", test[index].fitness());
//				}
//			}
			
			ThreadSafeRandom safeRandom = new ThreadSafeRandom();
			
			// 产生初始种群
			Chrom[] population = new Chrom[Var.POPU];
			for ( int i = 0; i < population.Length; i++ )
			{
				population[i] = new Chrom(Data.score.GetLength(0), Data.max_score, Data.score);
			}
			
			// 迭代
			List<Chrom> new_population = new List<Chrom>();
			for ( int g = 0; g < Var.GENE; g++ )
			{
				Console.WriteLine("g{0}", g);
				
				new_population.Clear();
				
				Console.WriteLine("selecting");
				for ( int i = 0; i < Var.POPU/2; i++ )
				{
					// 选择
					//Console.WriteLine("selecting {0}", i);
					var selected = Chrom.Select( population );
					if ( safeRandom.NextDouble() <= Var.PC )
					{
						var crossed = Chrom.Cross(selected.Item1, selected.Item2);
						new_population.Add(crossed.Item1);
						new_population.Add(crossed.Item2);
					}
					else
					{
						new_population.Add(selected.Item1);
						new_population.Add(selected.Item2);
					}
				}
				
				Console.WriteLine("sorting");
				new_population.Sort();
				Console.WriteLine("fitness {0}, {1}", new_population[new_population.Count-1].fitness(), new_population[new_population.Count-10].fitness());
				
				for ( int i = 1; i < new_population.Count; i++ )
				{
					if ( safeRandom.NextDouble() <= Var.PM )
					{
						new_population[i] = new Chrom(Data.score.GetLength(0), Data.max_score, Data.score);
					}
				}
				
				population = new_population.ToArray();
				
				//Chrom m = Chrom.Min(population);
				
			}
			
						
			Console.Write("Press any key to continue . . . ");
			Console.ReadKey(true);
		}
	}
}