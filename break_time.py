import time
import webbrowser

print('''>> Break Time Tracker initialized... <<
Started ''' + time.ctime())
hours_passed = 2
break_count = 1
while (break_count < 11):
    time.sleep(7200)
    print('''You\'ve been at your desk for {} hours!
    Get up and move around.
    This is break no.{} on''' + time.ctime()).format(hours_passed, break_count)
    webbrowser.open('https://www.youtube.com/watch?v=2m8qJbEY6lo')
    break_count +=1
    hours_passed += 2
    if (break_count == 10):
        print('That\'s it for today! No more breaks scheduled...')
