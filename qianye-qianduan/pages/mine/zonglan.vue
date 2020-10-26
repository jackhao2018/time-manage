<template>
	<view class="zonglan-body">
		<view class="kuai" v-for="(item,index) in obj" :index="index">
			<view class="head">
				{{item.title}}
			</view>
			<view class="box">
				<view class="img">
					<image src="" mode=""></image>
				</view>
				<view class="bottom">
					<view class="p">
						{{item.where}}
					</view>
					<view class="time">
						回归时间：{{item.time}}
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data(){
			return {
				obj:[
				{
					title:"背管理经记忆曲线",
					time:"09/11-10/15",
					where:"0911、0912、0914、0917、0925、0930、1015"
				},
				{
					title:"背管理经济学第五章",
					time:"09/11-10/15",
					where:"0911、0912、0914、0917、0925、0930、1015"
				},
				{
					title:"背管理经济学第五章",
					time:"09/11-10/15",
					where:"0911、0912、0914、0917、0925、0930、1015"
				}
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
	.zonglan-body {
		height: 100%;
		overflow-y: auto;
	}
	.kuai {
		width: 90%;
		margin: 20rpx 5%;
		box-sizing: border-box;
		padding: 30rpx;
		background-color: #EEEEEE;
	}
	.head {
		font-size: 36rpx;
		height: 30rpx;
		line-height: 36rpx;
		margin-bottom:30rpx;
		text-align: center;
	}
	.img {
		width: 100%;
		height: 100rpx;
		background-color: #2C405A;
	}
	image {
		width: 100%;
		height: 100%;
	}
	.p {
		font-size: 26rpx;
		margin-top: 18rpx;
		margin-bottom: 30rpx;
	}
	.time {
		font-size: 24rpx;
		color: #999999;
	}
</style>
