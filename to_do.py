task=[]


def add_task():
    task_=''+input('enter your task')
    task.append('○ '+task_)
    print(task)

def remove_task():
    for i in range(len(task)):
        print(f'{i+1} . {task[i]}')
    try:
        n=int(input())
    except:
        print('Enter the number')
        remove_task()
    if n>len(task):
        print('Enter a Valid number')
    else:
        task.pop(n-1)

def mark_as_done():
    for i in range(len(task)):
        print(f'{i+1} . {task[i]}')
    n=int(input('enter the number which you want to remove'))
    text=task[n-1]
    task[n-1]='● '+text[1:]

def show_list():
    for i in range(len(task)):
        print(f'{i+1} . {task[i]}')


def main():
    while True:
        print()
        print()
        print('-------------------------------------------')
        print('1.Add task')
        print('2.Remove Task')
        print('3.Mark as Done')
        print('4.Clear all task')
        print('5.Show List')
        try:
            choice=int(input('Enter your opration'))
        except:
            print('please Enter The Valid Opearaton')
            main()
        if choice>5:
            print('please Enter The Valid Opearaton')
            main()
        elif choice==1:
            add_task()
        elif choice==2:
            remove_task()
        elif choice==3:
            mark_as_done()
        elif choice==4:
            task=[]
        elif choice==5:
            show_list()
main()