/*
 * 由SharpDevelop创建。
 * 用户： pfermat
 * 日期: 2017/12/14
 * 时间: 10:55
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;
using System.Threading;
using System.Security.Cryptography;

public class ThreadSafeRandom : Random
{
	//This is the seed provider
	private static readonly RNGCryptoServiceProvider _global = new RNGCryptoServiceProvider();
	
	//This is the provider of randomness.
	//There is going to be one instance of Random per thread
	//because it is  declared as ThreadLocal<Random>
	private ThreadLocal<Random> _local = new ThreadLocal<Random>(() => {
		//This is the valueFactory function
		//This code will run for each thread to initialize each independent instance of Random.
		var buffer = new byte[4];
		//Calls the GetBytes method for RNGCryptoServiceProvider because this class is thread-safe
		//for this usage.
		_global.GetBytes(buffer);
		//Return the new thread-local Random instance initialized with the generated seed.
		return new Random(BitConverter.ToInt32(buffer, 0));
	});
	
	public override int Next()
	{
		return _local.Value.Next();
	}
	
	public override int Next(int maxValue)
	{
		return _local.Value.Next(maxValue);
	}
	
	public override int Next(int minValue, int maxValue)
	{
		return _local.Value.Next(minValue, maxValue);
	}
	
	public override double NextDouble()
	{
		return _local.Value.NextDouble();
	}
	
	public override void NextBytes(byte[] buffer)
	{
		_local.Value.NextBytes(buffer);
	}
}