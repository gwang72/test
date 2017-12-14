﻿/*
 * 由SharpDevelop创建。
 * 用户： pfermat
 * 日期: 2017/12/14
 * 时间: 22:18
 * 
 * 要改变这种模板请点击 工具|选项|代码编写|编辑标准头文件
 */

using System;

public static class Data
{
	public static int[] max_score = {14,12,12,12,12,12,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5};
	
	public static int[,] score = {
		{9,12,11,12,12,11,0,4,0,4,5,0,5,5,5,5,5,5,5,5,5,5},
		{9,12,12,12,12,11,0,0,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{8,6,12,3,12,11,0,0,0,4,5,5,5,0,5,5,5,5,5,5,5,5},
		{9,0,6,11,12,11,0,0,0,4,5,5,0,5,5,5,5,5,0,5,5,5},
		{9,12,12,12,11,12,0,4,4,4,5,0,5,5,5,5,5,5,5,5,5,5},
		{1,7,4,9,1,6,0,0,4,4,0,5,0,5,5,5,5,5,0,5,5,5},
		{4,12,10,3,8,11,0,4,4,4,5,5,5,0,0,5,5,5,5,5,5,5},
		{11,12,6,12,12,11,0,4,4,4,0,5,5,5,5,5,5,5,0,5,5,5},
		{5,12,9,4,1,11,4,4,0,4,5,5,0,5,5,0,5,5,0,5,5,5},
		{12,12,6,12,10,11,0,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{2,0,4,3,0,0,0,0,4,0,5,5,0,0,5,0,0,5,5,5,5,0},
		{4,6,7,12,8,11,0,0,4,0,5,0,5,0,5,0,0,5,0,0,5,5},
		{5,6,4,0,0,0,0,0,0,4,0,0,0,0,0,0,0,5,0,5,0,0},
		{1,0,4,10,6,9,0,0,4,4,5,0,0,0,0,5,0,5,0,5,0,5},
		{11,0,0,11,12,12,0,4,4,4,5,5,5,0,5,0,5,5,5,5,0,5},
		{0,0,4,11,12,12,4,0,4,4,5,0,5,0,5,0,0,5,5,5,5,5},
		{11,12,12,12,12,11,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{0,0,8,4,0,11,0,0,0,0,0,0,5,5,0,5,0,5,5,5,0,0},
		{9,12,12,12,12,11,0,0,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{4,12,7,12,4,11,0,0,0,4,0,0,5,5,5,5,5,5,0,5,5,5},
		{4,0,12,3,12,11,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{0,0,0,0,0,3,0,0,0,4,5,5,0,0,0,5,5,5,0,0,5,5},
		{1,12,0,11,11,11,0,0,0,4,0,0,0,0,0,5,5,5,0,5,5,5},
		{4,0,6,11,1,11,0,4,4,0,0,0,5,5,5,5,5,5,5,5,5,5},
		{7,0,4,11,1,6,0,0,4,4,5,0,5,5,5,5,5,5,5,0,5,5},
		{0,0,12,12,12,12,0,4,4,4,0,5,5,5,5,5,5,5,0,5,5,5},
		{4,12,5,1,8,12,0,0,4,4,5,5,5,5,5,0,5,5,0,0,0,5},
		{9,6,12,12,0,11,4,4,0,4,0,0,5,5,5,5,5,5,5,5,5,5},
		{10,6,12,12,12,7,4,0,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{10,12,6,5,1,11,0,0,0,0,0,5,5,0,5,5,5,0,0,5,0,5},
		{4,12,12,12,12,11,0,0,4,4,0,0,5,0,5,5,5,5,5,5,0,5},
		{6,12,0,12,12,8,0,4,4,4,5,5,5,0,5,5,5,5,5,5,5,5},
		{6,12,11,11,12,11,4,4,4,4,5,5,0,0,5,5,5,5,5,5,5,5},
		{1,0,0,11,1,11,0,4,0,4,5,5,0,5,5,5,0,5,5,5,5,5},
		{5,12,10,8,12,9,0,0,4,4,5,0,0,5,5,0,5,5,5,5,5,5},
		{5,0,10,12,0,3,0,0,0,4,0,5,0,5,5,0,5,5,0,5,5,0},
		{10,12,10,10,0,11,0,4,4,0,5,0,0,0,5,5,5,5,0,5,5,5},
		{8,12,10,11,11,11,0,0,4,4,5,0,5,5,5,5,5,5,0,5,5,5},
		{10,12,12,12,1,12,0,0,4,0,5,0,5,0,5,5,5,5,5,5,5,5},
		{10,0,7,12,12,12,0,0,4,4,5,0,5,0,5,5,5,5,5,5,5,5},
		{11,12,6,12,12,11,0,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{1,12,12,12,12,3,0,0,0,4,0,0,0,5,5,0,5,5,0,5,5,5},
		{9,12,10,12,1,12,4,4,0,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{9,12,12,11,12,11,0,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{1,0,4,6,1,0,0,0,4,4,5,5,0,5,5,5,0,5,0,5,5,5},
		{10,12,6,12,12,12,4,4,0,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{9,12,12,12,8,1,4,4,0,4,5,5,5,5,5,5,5,5,0,5,5,5},
		{10,12,12,12,8,10,0,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{4,0,11,0,12,11,0,0,0,4,0,0,0,5,5,0,5,5,5,5,5,5},
		{5,2,5,12,12,11,0,4,4,4,5,0,5,5,0,0,5,5,5,5,0,5},
		{0,0,4,4,0,12,0,0,0,0,0,0,5,0,5,0,5,5,0,5,5,5},
		{9,0,11,12,0,0,0,4,4,4,0,5,5,5,5,5,5,5,5,5,5,5},
		{0,0,0,1,1,6,0,0,0,0,0,5,0,0,5,0,5,0,5,5,5,5},
		{0,0,0,11,1,6,0,0,4,4,0,0,0,0,5,0,0,5,5,0,0,5},
		{0,0,5,12,1,0,0,4,4,0,0,0,5,5,0,0,0,5,0,5,5,5},
		{0,7,6,11,0,1,0,4,0,0,5,0,0,5,0,0,0,5,0,5,5,5},
		{8,7,12,11,0,12,0,4,4,4,0,5,0,5,5,0,5,5,5,5,5,0},
		{4,12,4,12,11,0,0,0,4,0,5,0,0,5,5,0,5,5,0,5,5,5},
		{4,12,7,8,6,11,0,0,0,0,0,0,5,0,0,5,5,5,0,0,5,5},
		{0,0,0,1,1,5,0,0,0,0,0,5,0,5,5,0,0,5,0,0,5,0},
		{1,12,8,4,0,1,0,0,4,4,0,5,0,0,5,5,5,5,0,5,5,0},
		{1,0,4,12,0,6,0,4,4,4,5,0,5,5,5,5,5,5,5,5,5,0},
		{0,6,4,7,1,6,0,0,4,0,5,0,0,5,0,0,0,0,0,5,5,0},
		{4,0,0,0,0,6,0,0,4,0,5,5,0,0,5,0,0,5,5,5,5,0},
		{4,9,0,12,12,1,0,0,0,4,0,5,5,0,5,0,5,5,0,5,5,5},
		{5,0,4,12,1,9,0,0,4,4,0,0,5,5,5,0,5,5,5,5,5,5},
		{4,0,4,6,0,10,0,0,4,0,5,0,0,0,5,0,5,5,0,5,5,0},
		{6,12,7,12,12,7,0,4,4,4,5,5,0,5,5,5,5,5,5,5,5,5},
		{1,12,0,12,8,11,0,4,4,4,5,5,0,5,5,0,0,5,5,5,5,5},
		{0,0,0,12,8,11,0,0,4,4,0,0,5,5,5,5,5,5,0,5,0,5},
		{2,12,10,12,1,3,0,0,0,4,5,5,0,5,5,5,5,5,0,5,5,5},
		{11,12,7,12,12,12,0,0,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{1,0,12,0,12,12,0,0,4,4,5,0,5,5,5,0,5,5,5,5,5,5},
		{10,0,12,12,12,11,0,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{4,6,10,12,8,9,4,4,0,0,5,5,0,5,5,5,5,5,0,5,5,5},
		{10,0,11,12,12,11,0,0,0,0,5,5,0,0,0,0,5,5,5,0,5,5},
		{4,7,7,4,1,12,0,0,4,4,5,0,0,5,5,0,0,5,0,5,5,5},
		{0,5,4,12,12,11,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{8,12,12,1,12,11,0,4,0,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{10,0,5,12,1,12,0,0,4,4,5,5,0,5,5,5,5,5,5,5,5,5},
		{5,0,10,12,8,12,0,4,4,0,5,5,0,5,5,5,5,5,5,5,5,0},
		{7,0,12,12,12,11,0,4,4,4,5,5,0,0,5,5,5,5,5,5,5,5},
		{6,12,12,12,12,11,0,0,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{6,12,11,3,12,11,0,0,4,0,0,0,5,0,5,5,5,5,5,5,5,5},
		{10,12,12,12,12,12,0,4,4,4,5,5,0,0,5,5,5,5,5,5,5,5},
		{11,12,12,12,12,4,0,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{9,11,12,12,0,11,4,4,4,4,5,5,5,0,5,5,5,5,5,5,5,5},
		{1,0,0,10,1,11,0,4,4,4,5,0,0,5,5,5,5,5,5,5,5,5},
		{9,12,12,12,12,12,0,0,4,4,5,5,5,5,5,0,5,5,5,5,5,5},
		{4,12,12,12,12,10,4,0,4,4,5,5,0,5,5,5,5,5,5,5,5,5},
		{2,12,8,12,10,11,0,4,4,4,5,5,0,0,5,5,5,5,5,5,5,5},
		{4,0,12,12,6,11,4,0,4,4,5,5,5,5,5,0,5,5,5,5,5,5},
		{4,7,7,12,1,12,0,4,0,4,0,5,0,5,5,5,0,5,0,5,5,5},
		{5,6,11,12,12,12,0,0,4,4,5,5,5,5,5,5,5,5,0,5,5,5},
		{5,12,11,12,1,11,0,0,0,0,5,0,0,5,5,5,5,5,5,5,5,0},
		{3,12,4,12,8,11,0,0,4,0,0,0,0,5,5,5,5,5,0,5,5,0},
		{4,6,10,8,12,8,0,4,4,4,5,5,0,5,5,0,5,5,5,5,0,5},
		{10,12,12,12,0,11,0,0,4,4,0,5,0,0,5,5,5,5,5,5,5,5},
		{9,0,6,5,12,8,0,0,4,0,5,5,5,5,5,5,5,5,5,5,5,5},
		{9,0,8,12,10,11,0,0,4,4,5,5,5,5,0,0,5,5,0,5,5,5},
		{9,0,8,12,0,11,4,0,0,4,5,5,0,5,5,0,5,5,5,0,5,5},
		{0,0,10,11,12,11,0,0,0,4,5,5,5,5,5,0,5,5,5,5,5,5},
		{9,12,10,11,12,12,0,4,4,4,5,5,5,5,5,5,5,5,0,5,5,5},
		{4,0,8,6,1,11,0,0,4,4,0,5,0,5,5,5,5,5,5,5,5,5},
		{9,12,0,12,8,7,0,4,4,4,5,5,5,5,5,0,5,5,5,5,5,5},
		{3,9,7,12,12,11,0,0,4,4,5,5,5,5,5,0,5,5,5,5,5,5},
		{4,0,0,12,12,11,0,4,4,4,5,0,5,0,5,5,5,5,5,5,5,5},
		{1,7,4,0,12,11,0,0,4,4,5,5,5,0,5,5,5,5,5,5,5,5},
		{4,0,8,12,12,11,0,4,4,4,5,0,5,5,5,0,0,5,5,5,5,5},
		{4,0,6,12,1,11,0,0,4,4,5,0,5,5,5,0,5,5,5,5,0,5},
		{2,0,10,12,12,11,0,4,4,4,0,0,5,0,0,5,5,5,5,5,0,5},
		{0,0,4,11,0,11,0,4,0,4,0,0,5,5,5,5,5,5,5,5,5,5},
		{6,11,12,11,10,11,0,4,4,4,0,5,5,5,5,0,5,5,0,5,5,5},
		{5,0,6,12,1,11,0,0,4,4,0,5,5,5,0,0,5,5,5,5,5,5},
		{4,12,6,12,12,11,0,0,4,4,0,5,0,5,5,5,5,5,0,0,5,5},
		{11,12,5,11,1,6,0,0,4,4,5,5,0,5,5,5,5,5,5,5,5,5},
		{1,12,12,12,12,12,0,4,4,4,5,0,5,5,5,5,5,5,5,5,5,5},
		{4,0,10,12,12,6,0,4,0,4,5,5,5,5,5,0,0,5,5,5,5,5},
		{4,12,12,12,12,4,0,0,4,4,5,0,0,5,5,5,5,5,5,5,5,5},
		{10,12,6,8,12,12,0,0,4,4,5,0,0,5,5,5,5,5,5,5,5,5},
		{9,12,6,12,12,11,0,0,4,4,5,0,5,5,5,5,5,5,5,5,5,5},
		{10,12,12,12,12,12,0,4,4,4,5,5,5,5,5,5,5,5,0,5,5,5},
		{8,0,6,12,0,12,0,0,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{7,12,6,12,12,12,0,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{0,0,0,5,0,1,0,0,4,0,5,0,5,0,0,5,0,5,0,0,5,0},
		{0,0,12,3,0,3,0,0,0,0,0,0,0,5,0,5,0,5,0,5,5,5},
		{8,0,5,3,0,11,0,4,0,4,5,5,0,5,5,0,0,5,0,5,5,0},
		{4,0,0,11,1,11,0,0,0,4,0,5,5,5,5,0,5,5,5,5,5,5},
		{9,12,9,11,8,12,0,4,4,4,5,0,5,5,5,5,5,5,5,5,5,5},
		{0,0,10,1,12,11,0,4,4,4,5,0,5,0,5,0,5,5,5,5,5,5},
		{1,0,0,11,12,11,0,4,4,4,5,0,5,5,5,5,5,5,5,5,5,5},
		{3,0,0,12,2,4,0,0,4,4,5,5,0,5,5,0,5,5,5,5,5,5},
		{10,12,12,12,12,11,0,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{8,0,11,8,12,11,0,0,4,4,5,5,5,0,5,0,5,5,5,5,0,5},
		{1,0,4,10,0,1,0,0,0,0,0,5,0,5,0,0,0,5,5,5,0,5},
		{1,0,4,0,0,0,0,0,0,0,5,5,5,5,5,5,0,5,5,0,5,0},
		{0,0,6,11,0,2,0,4,0,0,5,0,0,5,5,5,0,5,5,5,0,0},
		{8,0,10,12,11,6,4,4,0,4,5,5,5,5,5,5,5,5,0,5,5,5},
		{5,0,12,12,12,11,0,0,0,4,5,0,5,5,5,5,5,5,5,5,5,5},
		{3,7,6,11,1,6,0,0,0,0,0,0,0,0,5,5,0,5,0,5,5,5},
		{0,6,4,2,6,6,0,0,0,4,0,5,0,5,0,5,5,5,0,5,5,5},
		{4,7,6,4,1,11,0,4,0,4,5,0,0,5,5,0,5,5,0,5,5,5},
		{1,12,11,6,12,8,0,0,4,4,0,5,0,5,5,0,5,5,0,5,5,5},
		{5,12,10,12,12,11,0,0,4,0,5,5,5,0,5,5,5,5,5,5,5,5},
		{1,12,12,4,12,9,0,4,4,4,5,0,5,5,5,5,5,5,5,5,5,5},
		{9,12,12,12,12,7,0,4,0,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{3,0,4,2,6,0,0,0,0,0,0,0,0,0,5,5,5,5,0,5,5,5},
		{0,0,5,2,1,6,0,0,0,4,0,0,0,5,5,5,0,5,5,0,5,5},
		{5,0,4,12,12,6,0,4,4,0,5,5,5,5,5,0,5,5,5,5,5,5},
		{5,12,12,0,12,2,0,0,4,4,0,0,5,5,5,0,5,5,5,5,5,5},
		{6,7,4,1,8,11,0,0,0,4,5,0,5,0,0,0,5,5,0,5,5,5},
		{7,0,5,12,11,11,0,4,4,4,5,5,5,5,5,5,0,5,5,5,5,5},
		{5,12,10,12,12,11,0,4,4,4,5,5,0,5,5,5,5,5,5,5,5,5},
		{6,0,12,12,8,11,0,0,4,4,5,0,0,5,5,5,0,5,5,5,5,5},
		{9,12,12,2,12,11,0,0,4,4,5,0,0,0,5,5,5,5,5,5,5,5},
		{5,0,5,12,1,11,0,0,4,4,5,0,0,5,5,0,5,5,0,5,5,5},
		{7,6,11,6,12,6,0,0,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{5,12,12,12,12,11,0,0,4,4,5,0,0,5,5,5,5,5,0,5,5,5},
		{0,12,10,12,1,5,0,0,4,0,0,5,0,5,5,0,0,5,5,5,5,5},
		{5,0,0,4,0,11,0,0,4,4,5,5,0,0,5,0,5,5,0,5,5,5},
		{0,12,7,12,12,11,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{5,6,12,12,12,0,0,0,4,4,5,5,5,5,5,0,5,5,5,5,5,5},
		{0,0,4,2,1,1,0,0,4,0,5,5,0,0,5,5,5,5,5,5,5,5},
		{5,12,10,12,6,11,0,0,4,4,5,5,5,5,5,5,5,5,5,5,5,5},
		{0,7,0,0,1,11,0,0,4,4,0,0,0,0,0,0,0,5,5,5,5,5},
		{3,7,6,12,1,5,0,0,4,4,5,0,5,0,5,5,5,5,0,5,5,5}
	};
}