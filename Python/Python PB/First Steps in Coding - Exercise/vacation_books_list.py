#	Брой страници в текущата книга – цяло число в интервала [1…1000]
#	Страници, които прочита за 1 час – цяло число в интервала [1…1000]
#	Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]
pages_sum = int(input())
pages_per_hour = int(input())
days_to_read = int(input())
#   Общо време за четене на книгата: 212 страници / 20 страници за час = 10 часа общо
#   Необходимите часове на ден: 10 часа / 2 дни = 5 часа на ден
hours_to_read_book = pages_sum // pages_per_hour
hours_need_per_day = hours_to_read_book // days_to_read
print(hours_need_per_day)