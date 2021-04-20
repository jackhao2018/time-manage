test_str = "(1451, 'Cannot delete or update a parent row: a fo…gy_id`) REFERENCES `strategys` (`strategy_id`))')"

if test_str.find('1451'):
    print('在里面')
else:
    print('木有')