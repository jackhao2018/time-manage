<template>
	<view class="container">
		<view class="top">
			<view class="naveget" v-for="(item,index) in data" @click="toMineSet(index)">
				{{item}}
			</view>
		</view>
		<view class="bottom">
			<view>
			    <uni-calendar 
			    :insert="true"
			    :lunar="true" 
			    :start-date="'2019-3-2'"
			    :end-date="'2019-5-20'"
			    @change="change"
			     />
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				data:["重要紧急","重要不紧急","紧急不重要","不紧急不重要"]
			}
		},
		methods: {
			toMineSet(id){
				uni.navigateTo({
					url: "./jinji?id="+id
				});
			}
		}
	}
</script>

<style>
	.container {
		height: 100%;
	}
	.top {
		margin: 20rpx;
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
	}
	.naveget {
		width: 45%;
		height: 188rpx;
		line-height: 150rpx;
		margin-bottom: 20rpx;
		text-align: center;
		box-sizing: border-box;
		border: 1rpx solid #09BB07;
	}
</style>
