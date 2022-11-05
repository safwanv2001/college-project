import os
from flask import *
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.secret_key="hgsd"
from src.dbconnection import *
@app.route('/add_attendance',methods=['get','post'])
def add_attendance():

    return render_template("Add attendance.html")


@app.route('/add_mark_staff',methods=['get','post'])
def add_mark_staff():
    qry="SELECT `subject`.* FROM `subject` JOIN `assign` ON `assign`.`subject_id`=`subject`.`subject_id` WHERE `assign`.`staff_id`=%s"
    res=selectall(qry,session['lid'])



    return render_template("Add mark staff.html",val=res)


@app.route('/searchstud', methods=['post'])
def searchstud():

    btn=request.form['btn']
    if btn=='Search':



        subject=request.form['select']
        qry = "SELECT `student`.* FROM `student` JOIN `subject` ON `subject`.`semester`=`student`.`semester` WHERE `subject`.`subject_id`=%s"
        val=(subject)
        res1 = selectall(qry, val)
        print(res1,"===============")
        qry = "SELECT `subject`.* FROM SUBJECT JOIN `assign` ON `assign`.`subject_id`=`subject`.`subject_id` JOIN `staff` ON `staff`.`staff_rid`=`assign`.`staff_id` WHERE `assign`.`staff_id`=%s"
        res = selectall(qry, session['lid'])


        return render_template("Add mark staff.html", val1=res1,val=res,subj=str(subject))
    else:

        try:
            subid = request.form['select']
            sid = request.form.getlist('name')
            mark = request.form.getlist('textfield')
            for i in range(0,len(sid)):
                print(sid[i],mark[i])
                qry="select * from mark where `subject_id`=%s AND `student_id`=%s AND DATE=curdate()"
                val=(subid,sid[i])
                res=selectone(qry,val)
                if res is None:

                    qry = "INSERT INTO `mark` VALUES(NULL,%s,%s,%s,%s,curdate())"
                    val = (session['lid'], subid, sid[i], mark[i])
                    iud(qry, val)

            return redirect('manage_mark#about')
        except Exception as e:

            return '''<script>alert('errr');window.location='manage_mark'</script>'''



@app.route('/add_mentor',methods=['get','post'])
def add_mentor():
    qry="select * from staff"
    res=select(qry)

    return render_template("Add mentor.html",val=res)
@app.route('/add_notification', methods=['get','post'])
def add_notification():

    return render_template("Add notification.html")
@app.route('/add_staff',methods=['get','post'])
def add_staff():

    return render_template("Add staff.html")
@app.route('/add_subject', methods=['get','post'])
def add_subject():

    return render_template("add subject.html")
@app.route('/add_subject_to_staff',methods=['get','post'])
def add_subject_to_staff():
    qry="select * from staff"
    res=select(qry)
    qry="select * from subject"
    ser=select(qry)
    return render_template("add subject to staff.html",val=res,lav=ser)
@app.route('/add_work.html', methods=['get','post'])
def add_work():

    return render_template("Add work.html")
@app.route('/admin_home',methods=['get','post'])
def admin_home():

      return render_template("admin home.html")
@app.route('/',methods=['get'])
def login():

    return render_template("Login.html")
@app.route('/manage_mentor',methods=['get','post'])
def manage_mentor():
    qry="SELECT `staff`.*,`mentor`.* FROM `staff` JOIN `mentor` ON `staff`.`staff_rid`=`mentor`.`staff_lid`"
    res=select(qry)
    return render_template("manage mentor.html",val=res)
@app.route('/manage_notification',methods=['get','post'])
def manage_notification():
    qry="select * from notification"
    res=select(qry)

    return render_template("manage notification.html",val=res)
@app.route('/manage_mark',methods=['get','post'])
def manage_mark():
    lid=session['lid']
    qry="SELECT * FROM `subject` WHERE `subject_id` IN(SELECT `subject_id` FROM `mark` WHERE `staff_id`=%s)"
    res=selectall(qry,lid)

    return render_template("manage mark.html",val=res)

@app.route('/searchmark',methods=['get','post'])
def searchmark():
    lid = session['lid']
    sub=request.form['select']
    qry="SELECT * FROM `subject` WHERE `subject_id` IN(SELECT `subject_id` FROM `mark` WHERE `staff_id`=%s)"
    res1=selectall(qry,lid)

    print(res1,"=============================")



    qry = "SELECT * FROM `student` JOIN `mark` ON `student`.`student_lid`=`mark`.`student_id` where `mark`.`subject_id`=%s"
    res = selectall(qry, sub)
    print(res,"===================================+++++++")
    return render_template("manage mark.html",val=res1,val1=res,s=str(sub))


@app.route('/manage_staff',methods=['get','post'])
def manage_staff():
    qry="select * from staff"
    res=select(qry)

    return render_template("manage staff.html",val=res)
@app.route('/manage_student',methods=['get','post'])
def manage_student():
    qry="SELECT `student`.*,`parent`.* FROM `student` JOIN `parent` ON `student`.`student_lid`=`parent`.`student_id`"
    res=select(qry)

    return render_template("Manage Student.html",val=res)
@app.route('/manage_subject',methods=['get','post'])
def manage_subject():
    qry="select * from subject"
    res=select(qry)
    return render_template("manage subject.html",val=res)
@app.route('/manage_assigned_staff',methods=['get','post'])
def manage_assigned_staff():
    qry="SELECT `staff`.*,`assign`.*,`subject`.* FROM `staff` JOIN `assign` ON `staff`.staff_rid=`assign`.staff_id JOIN `subject` ON `subject`.`subject_id`=`assign`.`subject_id`"
    res=select(qry)

    return render_template('/manage assigned staff.html',val=res)
@app.route('/manage_timetable',methods=['get','post'])
def manage_timetable():
    qry="select * from timetable"
    res=select(qry)

    return render_template("manage timetable.html",val=res)
@app.route('/parent_home',methods=['get','post'])
def parent_home():

    return render_template("Parent home.html")
@app.route('/parent_registration',methods=['get','post'])
def parent_registration():

    return render_template("parent registration.html")
@app.route('/staff_home',methods=['get','post'])
def staff_home():

    return render_template("Staff home.html")
@app.route('/staff_login',methods=['get','post'])
def staff_login():

    return render_template("Staff login.html")
@app.route('/add_student',methods=['get','post'])
def add_student():

    return render_template("Add student.html")

@app.route('/add_parent',methods=['get','post'])
def add_parent():

    return render_template("Add parent.html")

@app.route('/student_home',methods=['get','post'])
def student_home():

    return render_template("Student home.html")
@app.route('/add_timetable',methods=['get','post'])
def add_timetable():

    return render_template("add timetable.html")
@app.route('/logincode',methods=['get','post'])
def logincode():
    uname=request.form['textfield']
    password=request.form['textfield2']
    qry="select * from login where username=%s and password=%s"
    val=(uname,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid");window.location='/' </script>'''
    elif res[3]=='admin':
        session['lid'] = res[0]
        return '''alert("welcome")<script>window.location='/admin_home'</script>'''
    elif res[3]=='staff':
        session['lid']=res[0]
        return '''alert("welcome")<script>window.location='/staff_login'</script>'''
    else:
        return '''<script>alert("invalid");window.location='/' </script>'''



@app.route('/adding_staff',methods=['post'])
def adding_staff():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    gender=request.form['radiobutton']
    dob=request.form['textfield3']
    place=request.form['textfield4']
    post=request.form['textfield5']
    pin=request.form['textfield6']
    phone=request.form['textfield7']
    email=request.form['textfield8']
    username=request.form['textfield9']
    password=request.form['textfield10']
    qry="insert into login values(NULL,%s,%s,'staff')"
    val=(username,password)
    id=iud(qry,val)
    qry="insert into staff values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(id),fname,lname,gender,dob,place,post,pin,phone,email)
    iud(qry,val)
    return redirect('/manage_staff#about')

@app.route('/adding_student', methods=['post'])
def adding_student():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    gender=request.form['radiobutton']
    dob=request.form['textfield3']
    place=request.form['textfield4']
    post=request.form['textfield5']
    pin=request.form['textfield6']
    semester = request.form['select']
    phone=request.form['textfield7']
    email=request.form['textfield8']
    username=request.form['textfield9']
    password=request.form['textfield10']
    qry="insert into login values (NULL,%s,%s,'student')"
    val=(username,password)
    id=iud(qry,val)
    session['sid']=id
    qry="insert into student values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(id),fname,lname,gender,dob,place,post,pin,semester,phone,email)
    iud(qry,val)

    return redirect('/add_parent#about')

@app.route('/adding_parent',methods=['post'])
def adding_parent():
    sid=session['sid']
    f_name=request.form['textfield']
    l_name = request.form['textfield2']
    place = request.form['textfield4']
    post = request.form['textfield5']
    pin = request.form['textfield6']
    phone = request.form['textfield7']
    email = request.form['textfield8']
    username = request.form['textfield9']
    password = request.form['textfield10']
    qry="insert into login values(NULL,%s,%s,'parent')"
    val=(username,password)
    id=iud(qry,val)
    qry="insert into parent values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(id),f_name,l_name,place,post,pin,phone,email,str(sid))
    iud(qry,val)

    return redirect('/manage_student#about')

@app.route('/search_subject',methods=['post'])
def search_subject():
    semester=request.form['select']
    qry="select * from subject where semester=%s"
    val=(semester)
    res=selectall(qry,val)
    return render_template("manage subject.html",val=res)
@app.route('/adding_subject',methods=['post'])
def adding_subject():
    try:
        semester=request.form['select']
        subject=request.form['textfield']
        subcode=request.form['textfield2']
        qry="insert into subject values(NULL,%s,%s,%s)"
        val=(semester,subject,subcode)
        iud(qry,val)
        return redirect('/manage_subject#about')
    except Exception as e:
        return '''<script>alert('subject code already exist');window.location='manage_subject'</script>'''

@app.route('/adding_subject_to_staff',methods=['post'])
def adding_subject_to_staff():


    staffid=request.form['select']
    subjectid=request.form['select3']
    qry = "SELECT * FROM `assign` WHERE staff_id=%s OR subject_id=%s"
    val=(staffid,subjectid)
    res=selectone(qry,val)
    if res is None:

        qry="insert into assign values(NULL,%s,%s)"
        val=(staffid,subjectid)
        iud(qry,val)

        return redirect('/manage_assigned_staff#about')
    else:
        return '''<script>alert('Subject Already Assigned');window.location='manage_assigned_staff'</script>'''


@app.route('/adding_notification',methods=['post'])
def adding_notification():
    notification=request.form['textfield']
    qry="insert into notification values(NULL,curdate(),%s)"
    val=(notification)
    iud(qry,val)
    return redirect('/manage_notification#about')
@app.route('/adding_mentor',methods=['post'])
def adding_mentor():
    mentor=request.form['select']
    qry="insert into mentor values(NULL,%s)"
    val=(mentor)
    iud(qry,val)
    return redirect('/manage_mentor#about')
@app.route('/adding_timetable',methods=['post'])
def adding_timetable():
    sem=request.form['select']
    timetable=request.files['file']
    fn=secure_filename(timetable.filename)
    timetable.save(os.path.join('static/timetable',fn))
    qry="insert into timetable values(NULL,%s,%s)"
    val=(sem,fn)
    iud(qry,val)
    return redirect('/manage_timetable#about')

# @app.route('/search_mark',methods=['post'])
# def search_mark():
#
#     return render_template("Add mark staff.html")

@app.route('/edit_mark/<id>')
def edit_mark(id):
    # id=request.args.get('id')
    print(id)
    session['mid']=id
    qry="SELECT `mark`.*,`student`.* FROM `mark` JOIN `student` ON `student`.`student_lid`=`mark`.`student_id` WHERE mark.mark_id= %s"
    print(qry)
    res=selectone(qry,id)

    return render_template("edit mark.html",val=res)

@app.route('/editing_mark',methods=['post'])
def editing_mark():
    mark=request.form['textfield']
    qry="UPDATE `mark` SET `mark`=%s WHERE `mark_id`=%s"
    val=(mark,session['mid'])
    iud(qry,val)
    return redirect('/manage_mark#about')

@app.route('/delete_staff')
def delete_staff():
    id=request.args.get('id')
    qry="delete from staff where staff_rid=%s"
    iud(qry,id)
    qry="delete from login where id=%s"
    iud(qry,id)

    return redirect('manage_staff#about')

@app.route('/delete_mark')
def delete_mark():
    id = request.args.get('id')
    qry = "delete from mark where mark_id=%s"
    iud(qry, id)

    return redirect('manage_mark#about')

@app.route('/delete_subject')
def delete_subject():
    id=request.args.get('id')
    qry="delete from subject where subject_id=%s"
    iud(qry,id)
    qry="DELETE FROM `assign` WHERE subject_id=%s"
    iud(qry, id)

    return redirect('manage_subject#about')
@app.route('/delete_mentor')
def delete_mentor():
    id=request.args.get('id')
    qry="delete from mentor where subject_id=%s"
    iud(qry,id)

    return redirect('manage_mentor#about')
@app.route('/remove_notification')
def remove_notification():
    id=request.args.get('id')
    qry="delete from notification where n_id=%s"
    iud(qry,id)
    return redirect('/manage_notification#about')
@app.route('/remove_mentor')
def remove_mentor():
    id=request.args.get('id')
    qry="delete from mentor where mentor_id=%s"
    val=str(id)
    iud(qry,val)
    return redirect('/manage_mentor#about')
@app.route('/remove_timetable')
def remove_timetable():
    id=request.args.get('id')
    qry="delete from timetable where t_id=%s"
    iud(qry,id)
    return redirect('/manage_timetable#about')
@app.route('/remove_assigned_staff')
def remove_assigned_staff():
    id=request.args.get('id')
    qry="delete from assign where assign_id=%s"
    iud(qry,id)
    return redirect('/manage_assigned_staff#about')
@app.route('/delete_student')
def delete_student():
    id=request.args.get('id')
    qry="delete from student where student_lid=%s"
    iud(qry,id)
    qry="delete from login where id=%s"
    iud(qry,id)
    qry="delete from parent where student_id=%s"
    iud(qry,id)
    return redirect('/manage_student#about')
@app.route('/edit_staff')
def edit_staff():
    id=request.args.get('id')
    session['sid']=id
    qry="select * from staff where staff_rid=%s"
    res=selectone(qry,str(id))

    return render_template("Edit staff.html",val=res)
@app.route('/editing_staff',methods=['post'])
def editing_staff():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    gender = request.form['radiobutton']
    dob = request.form['textfield3']
    place = request.form['textfield4']
    post = request.form['textfield5']
    pin = request.form['textfield6']
    phone = request.form['textfield7']
    email = request.form['textfield8']
    qry = "UPDATE `staff` SET `f_name`=%s,`l_name`=%s,`gender`=%s,`dob`=%s,`place`=%s,`post`=%s,`pin`=%s,`phone`=%s,`email`=%s WHERE staff_rid=%s"
    val = (fname, lname, gender, dob, place, post, pin, phone, email,session['sid'])
    iud(qry, val)

    return redirect('/manage_staff#about')

@app.route('/edit_student')
def edit_student():
    id=request.args.get('id')
    session['sid']=id
    qry="select * from student where student_lid=%s"
    res=selectone(qry,str(id))

    return render_template("Edit student.html",val=res)

@app.route('/edit_parent')
def edit_parent():

    id=session['sid']
    qry="select * from parent where student_id=%s"
    res=selectone(qry,str(id))

    return render_template("edit parent.html",val=res)

@app.route('/editing_student',methods=['post'])
def editing_student():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    gender = request.form['radiobutton']
    dob = request.form['textfield3']
    place = request.form['textfield4']
    post = request.form['textfield5']
    pin = request.form['textfield6']
    phone = request.form['textfield7']
    email = request.form['textfield8']
    semester = request.form['select']
    qry="UPDATE `student` SET `f_name`=%s,`l_name`=%s,`gender`=%s,`dob`=%s,`place`=%s,`post`=%s,`pin`=%s, `semester`=%s, `phone`=%s,`email`=%s WHERE `student_lid`=%s"
    val= (fname, lname, gender, dob, place, post, pin, semester,phone, email,session['sid'])
    iud(qry,val)

    return redirect('/edit_parent#about')
@app.route('/editing_parent',methods=['post'])
def editing_parent():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    place = request.form['textfield4']
    post = request.form['textfield5']
    pin = request.form['textfield6']
    phone = request.form['textfield7']
    email = request.form['textfield8']
    qry="UPDATE `parent` SET `f_name`=%s,`l_name`=%s,`place`=%s,`post`=%s,`pin`=%s, `phone`=%s,`email`=%s WHERE `student_id`=%s"
    val= (fname, lname, place, post, pin,phone, email,session['sid'])
    iud(qry,val)

    return redirect('/manage_student#about')







app.run(debug=True)