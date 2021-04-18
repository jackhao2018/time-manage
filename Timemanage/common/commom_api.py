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
        num_list = list()
        init_day = self.today
        if len(i) > 1:
            while init_day <= self.end_date.date():
                if init_day.weekday() in i:
                    num = (init_day - self.today).days
                    num_list.append(num)
                init_day += datetime.timedelta(days=1)
            return num_list
        else:
            while self.begin_date.weekday() != i[0]:
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
            if len(num) == 1:
                for i in details_list[1:]:
                    date = first_date + datetime.timedelta(i)
                    date_list.append(date.isoformat())
            else:
                for i in details_list:
                    date = self.today + datetime.timedelta(days=i)
                    date_list.append(date.isoformat())

        return date_list