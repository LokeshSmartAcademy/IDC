import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import DictationCard, ExamCardDetails, StudentEnroll, DictationAudio, TestSchedule ,StudentTestStats, TestMarks
from .forms import StuEnroll, SclEnroll
from json import dumps , loads 
from django.core import serializers



# Create your views here.
@login_required
def index(request):
    dict1 = DictationCard()
    dict1.name = "DivaSree"
    dict1.id="ST_123"
    dict1.standard = "Class V"
    dict1.subject = "Telugu"
    dict1.levels ="Level 1"
    dict1.link ="www.fb.com"
    dict1.isschool= False

    dict2 = DictationCard()
    dict2.name = "Lokeshvarma"
    dict2.id="ST_1234"
    dict2.desc = "Never GiveUP"
    dict2.link ="www.instagram.com"
    dict2.isschool = False


    dict3 = DictationCard()
    dict3.name = "Himaja School"
    dict3.id="SC_14"
    dict3.desc = "Class V, Section B"
    dict3.link ="www.google.com"
    dict3.isschool = True

    if request.method =="POST":
        import pdb; pdb.set_trace()
    levels = ExamCardDetails.objects.all()
    dicts = list((dict1, dict2, dict3))
    now = datetime.datetime.now()
    upcoming = TestSchedule.objects.filter(scheduled_date__gte=now, status=1).order_by('scheduled_date', 'time_from')
    passed = TestSchedule.objects.filter(scheduled_date__lt=now, status=1).order_by('-scheduled_date', 'time_from')
    scheds = list(upcoming) + list(passed)
    return render(request, 'index.html', {'dicts': dicts, 'levels': levels, 'scheds' : scheds[:5]})

@login_required
def dictationaudio(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        # audio_lists = DictationAudio.objects.all()
        # level = "Dwithhaalu"
        testtype = request.POST.get('test_type')
        sk = request.POST.get('sk')
        sub = request.POST.get('sub', "Telugu")
        level = request.POST.get('level')
        tim = request.POST.get('times')
        times = int(tim)
        gap_check = request.POST.get('gapcheck')
        if gap_check:
            gap_s = request.POST.get('customgap',2)
        else:
            gap_s = request.POST.get('optiongap',2)    
        gap = float(gap_s) *1000

        stuobj = StudentEnroll.objects.get(sk=sk)
        stats = StudentTestStats()
        stats.name = stuobj
        stats.subject = sub
        stats.testtype = testtype
        stats.conductedBy = request.user
        stats.action = "started"
        stats.datenow = datetime.datetime.now
        stats.level = level
        stats.times = times
        stats.timegap = gap_s
        stats.status = 2
        stats.save()

        context = {'sk': sk , 'sub' : sub , 'level' : level ,'testtype' : testtype }
        data_test = serializers.serialize("json", DictationAudio.objects.filter(audio_level=level))
        data_test_1 = loads(data_test)
        final_list = []
        for data in data_test_1:
            hello = data.get('fields')
            hello["audio_path"] = 'media/' + hello["audio_path"]
            for i in range(int(times)):
                final_list.append(hello)
        data = dumps(final_list)    
        return render(request, 'dictation_audio.html',{'data' : data, 'gap': gap , 'times': times, 'context': context} )
    return redirect('/')        

@login_required
def enroll(request):
    if request.method == "POST":
        # import pdb; pdb.set_trace()
        if request.POST.get('stuname') :
           stu_class = request.POST.get('stuclass')
           max_class = StudentEnroll.objects.filter(stuclass=stu_class)
           if max_class:
               m_id = max_class.order_by("-sk")[:1].values_list('sk').get()[0]
               max_id = int(m_id.split('_')[-1])
           else:
               max_id = 0
           now = datetime.datetime.now()
           ijk = str(now.year)[-2:]
           final_sk = "L" + str(ijk)+"C"+ str(stu_class) +"_"+ str(max_id+1)
           form = StuEnroll(request.POST)
           if form.is_valid():
               name = form.cleaned_data.get('stuname')
               clas = form.cleaned_data.get('stuclass')
               schl = form.cleaned_data.get('stuschool')
               town = form.cleaned_data.get('stutown')
               contact = form.cleaned_data.get('stucontact')
               mail = form.cleaned_data.get('stuemail')
               sk = final_sk
               instance = StudentEnroll(stuname=name, stuclass=clas, stucontact=contact, stuemail=mail, stuschool=schl, stutown=town, sk = sk)
               instance.save()

               marks = TestMarks()
               marks.student = instance
               marks.save()

               return redirect('enroll')  
           else:
                return redirect('/')  

        elif request.POST.get('sclname'):
            form = SclEnroll(request.POST)        
            if form.is_valid():
                form.save()
                return redirect('/')  
            else:
                print("dobbbei")      
    else:
        form = StuEnroll()
    return render(request, 'enroll.html',{'form': form} )

def marksinit(request,sk):
    try:
        student = StudentEnroll.objects.get(sk = sk)
        marks = TestMarks()
        marks.student = student
        marks.save()
        print("Intialzed")
    except:
        pass
    return redirect(studentprofile, sk)

def marksupdate(request,sk):
    if request.method == "POST":
        student = StudentEnroll.objects.get(sk=sk)
        level = request.POST.get('level')
        marks = request.POST.get('marks')
        test_type , test_level = level.split('_')
        print(test_level, test_type)
        # import pdb; pdb.set_trace()
        dic1 = {'l1' : 'Sunnapadaalu', 'l2' : 'Dheergaalu', 'l3': 'Dwithhaalu', 'l4' : 'Samukthaalu', 'l5' : 'MahaPranalu', 'l6': 'Sa,Sha,Ha lu'}
        stusched = TestSchedule.objects.filter(name= student, status=3 , test_level= dic1.get(test_level), test_type=test_type)
        if stusched:
            student = StudentEnroll.objects.get(sk = sk)
            markobj = TestMarks.objects.filter(student=student).update(**{level: marks})
            msg = "Updated the Marks"

        else:
            msg = " * Cannot Update Marks Until Test Done"
            messages.info(request, msg)
        print(level, marks)
        return redirect(studentprofile, sk)  

@login_required
def dashboard(request):
    student_details_1 = StudentEnroll.objects.all()
    # student_details_2 = StudentEnroll.objects.filter(is_active=False)
    return render(request, 'dashboard.html',{'students': student_details_1} )

@login_required
def schedules(request):
    now = datetime.datetime.now()
    todayscheds = TestSchedule.objects.filter(scheduled_date=now.date(),status=1 ).order_by('time_from')
    upcoming = TestSchedule.objects.filter(scheduled_date__gt=now, status=1).order_by('scheduled_date', 'time_from')
    passed = TestSchedule.objects.filter(scheduled_date__lt=now, status=1).order_by('-scheduled_date', 'time_from')
    cancelled = TestSchedule.objects.filter(status=9).order_by('-scheduled_date', 'time_from')
    completed = TestSchedule.objects.filter(status=3).order_by('-scheduled_date', 'time_from')


    context =  {'upcoming': upcoming, 'passed': passed, 'todayscheds' : todayscheds, 'cancelled' : cancelled, 'completed' : completed}
    return render(request, 'schedules.html', context)    


@login_required
def schedule(request):
    student_details_1 = StudentEnroll.objects.filter(is_active= True)
    if request.method =="POST":
        student = request.POST.get('selected_student')
        subject = request.POST.get('selected_subject')
        test_type = request.POST.get('test_type')
        test_level = request.POST.get('test_level')
        scheduled = request.POST.get('scheduled_date')
        time_from = request.POST.get('time_from')
        time_to = request.POST.get('time_to')
        dum = StudentEnroll.objects.filter(sk = student).get()
        exists = TestSchedule.objects.filter(name=dum, subject=subject, test_type=test_type, test_level=test_level)
        
        if request.POST.get('reschedule'):
            resched = TestSchedule.objects.get(name=dum, subject=subject, test_type=test_type, test_level=test_level)
            resched.status = 1
            resched.time_to = time_to
            resched.time_from = time_from
            resched.scheduled_date = scheduled
            resched.save()

            stats = StudentTestStats()
            stats.name = dum
            stats.subject = subject
            stats.testtype = test_type
            stats.level = test_level
            stats.status = 1
            stats.action = "re-scheduled"
            stats.conductedBy = request.user
            stats.save()
            print("stats saved")
        
        else:    

            if exists:
                msg = " * This Scedule alreadi Exists * "
                messages.info(request, msg)
                print("Canot Schedule 2 times")
                return redirect('schedule')
            else:
                print('Success')    
                nickname_dict = {'l1': 'Sunn PRE', 'l2': 'Dhee PRE', 'l3': 'Dwit PRE', 'l4' : 'Sam PRE','l5' : 'Maha PRE', 'l6': 'Sa,Sha PRE',
                                'l7': 'Sunn POT', 'l8': 'Dhee POT', 'l9' : 'Dwit POT', 'l10': 'Sam POT', 'l11': 'Maha POT', 'l12': 'Sa,Sha POT',
                                'l13': 'Sunn POOT', 'l14' : 'Dhee POOT', 'l15': 'Dwit POOT', 'l16': 'Sam POOT', 'l17': 'Maha POOT', 'l18': 'Sa,Sha POOT',
                                'l19' : 'Sunn POST', 'l20': 'Dhee POST', 'l21': 'Dwit POST', 'l22': 'Sam POST', 'l23': 'Maha POST', 'l24': 'Sa,Sha POST'
                                }

                for nick, value in nickname_dict.items():
                    lev , exam = value.split(' ')
                    if lev in test_level and exam in test_type:
                        nick_name = nick
                        break                   

                test = TestSchedule()
                test.time_to = time_to
                test.time_from = time_from
                test.scheduled_date = scheduled
                test.subject = subject
                test.test_nickname = nick_name
                test.test_type = test_type
                test.test_level= test_level
                test.name = dum
                test.save()
                # import pdb; pdb.set_trace()

                stats = StudentTestStats()
                stats.name = dum
                stats.subject = subject
                stats.testtype = test_type
                stats.level = test_level
                stats.status = 1
                stats.action = "scheduled"
                stats.conductedBy = request.user
                stats.save()
                print("stats saved")
    return render(request, 'schedule.html',{'students': student_details_1} )

@login_required
def testinputs(request):
        # obj = StudentEnroll.objects.get(sk=sk)
        if request.method == "POST":
            print(request.POST)
            studentsk = request.POST.get('studentsk')
            stuname = request.POST.get('studentname')
            subject = request.POST.get('subject')
            level = request.POST.get('level')
            test_type = request.POST.get('test_type')
            obj = { 'sk' : studentsk, 'sub' : subject, 'test_type' : test_type, 'name' : stuname, 'level': level}
            if request.POST.get('starttest') or request.POST.get('go'):
                return render(request, 'testinputs.html', obj)
            elif request.POST.get('reschedule'):
                return render(request, 'reschedule.html', obj) 
            elif request.POST.get('delete'): 
                dum = StudentEnroll.objects.filter(sk = studentsk).get()
                schedule = TestSchedule.objects.get(name=dum, subject=subject, test_type=test_type, test_level=level)
         
                stats = StudentTestStats()
                stats.name = dum
                stats.subject = subject
                stats.testtype = test_type
                stats.level = level
                stats.status = 0
                stats.action = "deleted"
                stats.conductedBy = request.user
                stats.save()
                print("stats saved")

                schedule = TestSchedule.objects.get(name=dum, subject=subject, test_type=test_type, test_level=level)
                schedule.delete()
                print('deleted')
                return redirect('schedules')     
        else:
            return redirect('/')      


def appointment(request):
    return render(request, 'appointment.html')    

def audio_player(request):
    return render(request, 'audio_player.html')    

def letsmakefun(request):
    return render(request, 'letsmakefun.html')

@login_required
def studentprofile(request, sk):
    obj = StudentEnroll.objects.get(sk=sk)
    stats = StudentTestStats.objects.filter(name=obj).order_by('-datenow')
    try:
        marks = TestMarks.objects.get(student=obj)
    except:
        marks = {}
    context = {"student_meta" : obj , "student_stats": stats, "marks": marks}
    return render(request, "student_profile.html", context)

def statusupdate(request):
    if request.method == "POST":
        print(request.POST)
        sub = request.POST.get('sub')
        level = request.POST.get('level')
        sk = request.POST.get('sk')
        testtype = request.POST.get('test_type')

        stu_obj = StudentEnroll.objects.get(sk =sk)
        test_sched = TestSchedule.objects.get(name=stu_obj, subject=sub, test_level=level, test_type=testtype)

        state = request.POST.get('status')
        if state == "end":
            status = 9
            action = "quitted"
        elif state == "success":
            action = "conducted"
            status = 3
        test_sched.status = status  
        test_sched.save()


        stuobj = StudentEnroll.objects.get(sk=sk)
        stats = StudentTestStats()
        stats.name = stuobj
        stats.subject = sub
        stats.action = action
        stats.testtype = testtype
        stats.conductedBy = request.user
        stats.datenow = datetime.datetime.now
        stats.level = level
        stats.status = status
        stats.save()






    return redirect('/')    



