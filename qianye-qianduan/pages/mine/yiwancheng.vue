<template>
	<view class="dai-body">
		<view class="kuai" v-for="(item,index) in obj" :index="index">
			<view class="p">
				{{item.title}}
			</view>
			<view class="time">
				时间：{{item.time}}
			</view>
			<view class="jieshi">
				复习时间点：{{item.where}}
			</view>
			<view class="xuanfu">
				已完成
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
					title:"背管理经济学第五章",
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
	.dai-body {
		height: 100%;
		overflow-y: auto;
	}
	.kuai {
		width: 90%;
		margin: 20rpx 5%;
		padding: 10rpx;
		background-color: #F6F6F6;
		position: relative;
	}
	.p {
		font-size: 14rpx;
		margin-bottom: 10rpx 0 20rpx 0;
	}
	.time,.jieshi {
		font-size: 12rpx;
		margin: 10rpx 0 10rpx 0;
	}
	.xuanfu {
		position: absolute;
		right: 80rpx;
		top: 42rpx;
		color: #B6B6B6;
		border: 1px solid #B6B6B6;
		font-size: 12rpx;
		padding: 8rpx;
		transform:rotate(-33deg);
	}
</style>
