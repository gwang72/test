/*
 * 由SharpDevelop创建。
 * 用户： pfermat
 * 日期: 2017/12/14
 * 时间: 10:52
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */
using System;

namespace paper
{
	class Program
	{
		public static void Main(string[] args)
		{
			//Console.WriteLine("Hello World!");
			
			Chrom[] test = new Chrom[10];
			
			for ( int i = 0; i < 10; i++ )
			{
				test[i] = new Chrom(Data.score.GetLength(0), Data.max_score, Data.score);
			}
			
			for ( int i = 0; i < 50; i++ )
			{
				for ( int index = 0; index < 10; index++ )
				{
					Console.WriteLine("{0}", test[index].fitness());
				}
			}
			
			Console.Write("Press any key to continue . . . ");
			Console.ReadKey(true);
		}
	}
}