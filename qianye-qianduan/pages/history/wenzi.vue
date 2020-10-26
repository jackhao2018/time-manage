<template>
	<view class="wenzi-body">
		<view class="top">
			<view class="title">
				艾兵豪斯记忆曲线
			</view>
			<view class="time">
				<view class="author">
					发布者：{{author}}
				</view>
				<view class="datetime">
					{{datetime}}
				</view>
				<view class="keep">
					已收藏
				</view>
			</view>
			<view class="neirong">
				{{data}}
			</view>
		</view>
		<view class="bottom">
			<input type="text" value="" />
			<view class="xinxi">
				<image src="" mode=""></image>
			</view>
			<view class="shou">
				<image src="" mode=""></image>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		onLoad: function (option) { //option为object类型，会序列化上个页面传递的参数
		    console.log(option.id); //打印出上个页面传递的参数。
		},
		data(){
			return {
				datetime:"2020-09-10 09:10:54",
				author:"阿尔法研究所",
				data:"会序列化上个页面传递的参数会序列化上个页面传递的参数会序列化上个页面传递的参数会序列化上个页面传递的参数会序列化上个页面传递的参数会序列化上个页面传递的参数会序列化上个页面传递的参数会序列化上个页面传递的参数会序列化上个页面传递的参数会序列化上个页面传递的参数会序列化上个页面传递的参数会序列化上个页面传递的参数会序列化上个页面传递的参数会序列化上个页面传递的参数会序列化上个页面传递的参数"
			}
		},
		methods:{
			// goDetailPage(e) {
			// 	let path = e.url ? e.url : e;
			// 	let url = ~path.indexOf('platform') ? path : '/pages/template/' + path + '/' + path;
			// 	uni.navigateTo({
			// 		url: url
			// 	});
			// 	return false;
			// }
		}
	}
</script>

<style>
	.wenzi-body {
		display: flex;
		height: 100%;
		flex-direction: column;
	}
	.top {
		flex: 1;
	}
	.bottom {
		height: 100rpx;
		display: flex;
		align-items: center;
	}
	.bottom input {
		height: 66rpx;
		flex: 1;
		background-color: #ECECEC;
		border: 1rpx solid  #ECECEC;
		border-radius: 4rpx;
		margin-left: 20rpx;
	}
	.bottom .xinxi {
		width: 50rpx;
		height: 50rpx;
		background-color: #000000;
		margin: 0 20rpx;
	}
	.bottom .shou {
		width: 50rpx;
		height: 50rpx;
		background-color: #000000;
		margin-right: 20rpx;
	}
	image {
		width: 100%;
		height: 100%;
	}
	.title {
		font-size: 36rpx;
		color: #313131;
		margin: 20rpx 20rpx;
	}
	.time {
		display: flex;
		font-size: 28rpx;
		color: #717171;
		height: 30rpx;
		line-height: 30rpx;
		margin-left: 20rpx;
		margin-right: 20rpx;
		padding-bottom: 30rpx;
		position: relative;
		border-bottom: 1rpx solid #DDDDDD;
	}
	.author {
		margin-right: 20rpx;
	}
	.keep {
		position: absolute;
		right: 0rpx;
		height: 30rpx;
		line-height: 30rpx;
		color: #B6B6B6;
		font-size: 20rpx;
		border: 1rpx solid #B6B6B6;
	}
	.neirong {
		margin: 20rpx;
		font-size: 28rpx;
		color: #313131;
	}
</style>
