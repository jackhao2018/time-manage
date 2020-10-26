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
	}
	.p {
		font-size: 14rpx;
		margin: 10rpx 0 20rpx 0;
	}
	.time,.jieshi {
		font-size: 12rpx;
		margin: 10rpx 0 10rpx 0;
	}
</style>
