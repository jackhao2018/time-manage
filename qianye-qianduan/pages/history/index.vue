<template>
	<view class="shoucang-body">
		<template v-for="(item,index) in obj" :index="index">
			<view class="kuai" @click="toMineSet(index)">
				<view class="img">
					<image>
					</image>
				</view>
				<view class="right">
					<view class="time">
						时间：{{item.time}}
					</view>
					<view class="jieshi">
						复习时间点：{{item.where}}
					</view>
				</view>
			</view>
			<view class="line"></view>
		</template>
		<view class="btn">
			查看更多
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
			toMineSet(id){
				uni.navigateTo({
					url: "./wenzi?id="+id
				});
			}
		}
	}
</script>

<style>
	.shoucang-body {
		height: 100%;
		overflow-y: auto;
	}
	.kuai {
		width: 90%;
		margin: 20rpx 5%;
		padding: 10rpx;
		background-color: #FFFFFF;
		display: flex;
	}
	.img {
		height: 100rpx;
		width: 100rpx;
		background-color: #333333;
		margin: 18rpx;
	}
	image {
		width: 100%;
		height: 100%;
	}
	.right {
		height: 100%;
		flex: 1;
	}
	.time,.jieshi {
		font-size: 12rpx;
		margin: 10rpx 0 10rpx 0;
	}
	.line {
		height: 16rpx;
		width: 100%;
		background-color: #ECECEC;
	}
	.btn {
		width: 112rpx;
		font-size: 13rpx;
		margin: 30rpx auto;
	}
</style>
