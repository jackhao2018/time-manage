# from datetime import datetime
# from datetime import date
import datetime

class GetStrategyDedail:

    today = datetime.date.today()

    def __init__(self, begin_date, end_date):
        self.begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    def fixed_interval(self, num):
        """
        固定间隔的类型，直接使用间隔数字
        :param num:间隔的天数
        :return:不同时间段内，对应策略的执行时间间隔列表
        """
        detail_list = list()
        date_num = (self.end_date - self.begin_date).days
        for i in range(num, date_num+1, num):
            detail_list.append(i)
        detail_list.insert(0, 0)
        return detail_list

    def weekly(self, i, weeks=1):
        """
        每周xx,每月xx的数据类型
        :param i：0-星期一，1-星期二，2-星期三，3-星期四，4-星期五，5-星期六，6-星期日
        :param weeks:间隔周数，默认间隔一周
        :return:不同时间段内，对应策略的执行时间间隔列表
        """
        while self.begin_date.weekday() != i:
            self.begin_date += datetime.timedelta(days=1)

        num = (self.begin_date.date() - self.today).days
        fixed_list = self.fixed_interval(weeks * 7)
        fixed_list.insert(0, num)

        return fixed_list

    def per_month(self, date):
        """
        date:指定要获取的每个月的日期
        :return:不同时间段内，对应策略的执行时间间隔列表
        """
        date_list = list()
        specific_list = list()
        year = self.begin_date.year
        begin_month = self.begin_date.month
        end_month = self.end_date.month
        day = self.end_date.day

        while begin_month <= end_month:
            designated_date = f'{year}-{begin_month}-{date}'
            date_list.append(datetime.datetime.strptime(designated_date, "%Y-%m-%d"))
            begin_month += 1

        for specific_date in date_list:
            num = (specific_date.date() - self.today).days
            if num > 0:
                specific_list.append(num)

        if day < date:
            specific_list.pop()

        return specific_list

    def make_date_from_list(self, num, interval=1, mode='day'):
        """
        :param interval: 间隔的周数，默认为1（每周）
        :param num:根据mode来区分，分表代表：间隔的天数，周几（0-6/周一-周日），指定的月日期
        :param mode:day, week, month
        :return: 不同时间段内，对应策略的执行时间间隔列表
        """
        date_list = list()

        if mode == 'day':
            details_list = self.fixed_interval(num)
        elif mode == 'week':
            details_list = self.weekly(num, interval)
        elif mode == 'month':
            details_list = self.per_month(num)

        first_date = self.today + datetime.timedelta(details_list[0])

        if mode == 'day':
            for i in details_list:
                date = self.begin_date.date() + datetime.timedelta(i)
                date_list.append(date.isoformat())
        elif mode == 'month':
            for i in details_list:
                date = self.today + datetime.timedelta(i)
                date_list.append(date.isoformat())
        else:
            for i in details_list[1:]:
                date = first_date + datetime.timedelta(i)
                date_list.append(date.isoformat())

        return date_list


# today = datetime.date.today()
# tomorrow = today + datetime.timedelta(days=1)
#
# # 或者4月1号到6月9号中，所有间隔为9天的日期
# print('\n每隔9天')
# print(GetStrategyDedail('2021-04-01', '2021-06-09').make_date_from_list(9, mode='day'))
#
# # 或者4月1号到6月9号中，所有每隔一个周日的日期
# print('\n每周日')
# print(GetStrategyDedail('2021-04-01', '2021-06-09').make_date_from_list(6, mode='week'))
#
# # 或者4月1号到6月9号中，所有每隔两个周末的周日日期
print('\n每两周的周六')
print(GetStrategyDedail('2021-04-05', '2021-09-30').make_date_from_list(5, 1, mode='week'))

# # 或者4月1号到6月8号中，每个月的9号
# print('\n每个月的9号')
# print(GetStrategyDedail('2021-04-01', '2021-08-08').make_date_from_list(9, mode='month'))
