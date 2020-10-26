<template>
	<view class="jinji-body">
		<view class="body1">
			<view class="xingqi">
				九月十日  周四
			</view>
			<view class="shijian">
				<view class="one" v-for="(item,index) in data" :index="index">
					{{item.title}}
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		onLoad(option) { //option为object类型，会序列化上个页面传递的参数
		    console.log(option.id); //打印出上个页面传递的参数。
			this.id = option.id;
		},
		data(){
			return {
				id:"",
				data:[
					{title:"2月份驾校考试，倒计时10天"},
					{title:"2月份驾校考试，倒计时10天"},
					{title:"2月份驾校考试，倒计时10天"},
					{title:"2月份驾校考试，倒计时10天"}
				]
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
	.jinji-body {
		background-color: #ECECEC;
		height: 100%;
	}
	.body1 {
		height: 100%;
		padding: 20rpx;
	}
	.xingqi {
		font-size: 36rpx;
		color: #313131;
		margin-left: 20rpx;
	}
	.shijian {
		background-color: #FFFFFF;
		border-radius: 4rpx;
		margin-top: 20rpx;
	}
	.one {
		height: 96rpx;
		margin: 0 20rpx;
		border-bottom: 1rpx solid #ECECEC;
		line-height: 96rpx;
	}
</style>
