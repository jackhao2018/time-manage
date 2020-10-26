<template>
	<view class="mine">
		<uni-list class="mine-background">
		    <uni-list-item @click="toMineSet('zonglan')"  title="策略总览" node="详细信息" rightText="详细信息" ></uni-list-item>
			<uni-list-item @click="toMineSet('shoucang')"  title="收藏" node="详细信息" rightText="详细信息" ></uni-list-item>
			<uni-list-item @click="toMineSet('yiwancheng')"  title="已完成" node="详细信息" rightText="详细信息" ></uni-list-item>
			<uni-list-item @click="toMineSet('daiwancheng')"  title="待完成" node="详细信息" rightText="详细信息" ></uni-list-item>
			<view class="line"></view>
			<uni-list-item  title="账户管理" node="详细信息" rightText="详细信息" ></uni-list-item>
			<view class="line"></view>
			<uni-list-item @click="toMineSet('set')"  title="设置" node="详细信息" rightText="详细信息" ></uni-list-item>
		</uni-list>
	</view>
</template>

<script>
	export default {
		data(){
			return {}
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
			toMineSet(url){
				uni.navigateTo({
					url: "./"+url
				});
			}
		}
	}
</script>

<style>
	.mine {
		height: 100%;
	}
	.mine .mine-background {
		height: 100%;
		background-color: #ECECEC;
	}
	.uni-list-item {
		background-color: #fff;
	}
	.line {
		height: 16rpx;
		width: 100%;
	}
</style>
