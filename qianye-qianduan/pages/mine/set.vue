<template>
	<view class="mine">
		<uni-list class="mine-background">
		    <uni-list-item  title="关闭高效四分图的动画效果" node="详细信息" rightText="详细信息" ></uni-list-item>
			<uni-list-item  title="XXXXXX特效关闭打开" node="详细信息" rightText="详细信息" ></uni-list-item>
			<uni-list-item  title="只显示某某模式" node="详细信息" rightText="详细信息" ></uni-list-item>
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
