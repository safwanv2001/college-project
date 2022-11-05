import os
from flask import *
from werkzeug.utils import secure_filename

app=Flask(__name__)
from src.dbconnection import *



@app.route('/logincode',methods=['post'])
def logincode():
    print(request.form)
    uname=request.form['uname']
    password=request.form['pswd']
    qry="select * from login where username=%s and password=%s"
    val=(uname,password)
    res=selectone(qry,val)
    if res is None:
        return jsonify({'task':'invalid'})
    else:
        id=res[0]
        type=res[3]
        return jsonify({'task': "valid","id":id,"type":type})

@app.route('/view_work',methods=['post'])
def view_work():
    sid=request.form['sid']
    # sem=request.form
    qry="SELECT * FROM `work` WHERE `staff_id`=%s"
    val=(sid)
    res=androidselectall(qry,val)
    return jsonify(res)

@app.route('/view_work_report',methods=['post'])
def view_work_report():
    wid=request.form['sid']
    print(wid,"====")
    qry="SELECT `workreport`.*,`student`.*,`work`.* FROM `workreport` JOIN `work` ON `work`.`work_id`=`workreport`.`work_id` JOIN `student` ON `student`.`student_lid`=`workreport`.`student_id` WHERE `work`.`staff_id`=%s"
    res=androidselectall(qry,wid)
    print(res,"===========")
    return jsonify(res)

@app.route('/view_allocated_subject',methods=['post'])
def view_allocated_subject():
    stid=request.form['stid']
    qry="SELECT `staff`.*,`assign`.*,`subject`.* FROM `staff` JOIN `assign` ON `staff`.staff_rid=`assign`.staff_id JOIN `subject` ON `subject`.`subject_id`=`assign`.`subject_id` WHERE `staff_rid`=%s"
    res=androidselectall(qry,stid)
    print(res)

    return jsonify(res)



@app.route('/view_subject',methods=['post'])
def view_subject():
    stid=request.form['lid']
    qry="SELECT `subject`.* FROM `subject` JOIN `student` ON `student`.`semester`=`subject`.`semester` WHERE `student`.`student_lid`=%s"
    res=androidselectall(qry,stid)
    print(res)

    return jsonify(res)





@app.route('/manage_work',methods=['post'])
def manage_work():
    stid=request.form['stid']
    sem=request.form['sem']
    qry="SELECT * FROM `work` WHERE `staff_id`=%s AND `sem`=%s"
    val=(stid,sem)
    res=androidselectall(qry,val)
    return jsonify(res)

@app.route('/add_work',methods=['post'])
def add_work():
    stid=request.form['stid']
    work=request.form['work']
    sub=request.form['subid']
    subdate = request.form['subdate']
    qry="insert into `work` values(NULL,%s,%s,curdate(),%s,%s)"
    val=(stid,work,subdate,sub)
    iud(qry,val)
    return jsonify({'task':'task success'})

@app.route('/add_work_report',methods=['post'])
def add_work_report():
    wid=request.form['wid']
    lid=request.form['lid']
    work_report = request.files['file']
    fn = secure_filename(work_report.filename)
    work_report.save(os.path.join('static/work_report', fn))
    q="SELECT * FROM `workreport` WHERE `work_id`=%s AND `student_id`=%s"
    v=(wid,lid)
    res=selectone(q,v)
    if res is None:
        qry="insert into `workreport` values(NULL,%s,%s,%s,curdate())"
        val=(wid,lid,fn)
        iud(qry,val)
        return jsonify({'task':'success'})
    else:
        return jsonify({'task':'Already added!!!'})


@app.route('/view_attendance_student',methods=['post'])
def view_attendance_student():
    stid=request.form['stid']
    mnth = request.form['mnth']
    print(request.form)
    if mnth == 'january':
        mnth = 1
    elif mnth == 'february':
        mnth = 2
    elif mnth == 'march':
        mnth = 3
    elif mnth == 'april':
        mnth = 4
    elif mnth == 'may':
        mnth = 5
    elif mnth == 'june':
        mnth = 6
    elif mnth == 'july':
        mnth = 7
    elif mnth == 'august':
        mnth = 8
    elif mnth == 'september':
        mnth = 9
    elif mnth == 'october':
        mnth = 10
    elif mnth == 'november':
        mnth = 11
    elif mnth == 'december':
        mnth = 12

    qry = "SELECT COUNT(`attendance`) AS twh,SUM(`attendance`) AS tph,(SUM(`attendance`)/COUNT(`attendance`))*100 AS pe,(COUNT(`attendance`)-SUM(`attendance`)) AS ah ,`student`.* FROM `attendance` JOIN `student` ON `student`.`student_lid`=`attendance`.`student_id` WHERE MONTH(DATE)=%s AND  `student`.`student_lid`=%s  GROUP BY DATE"
    val = (mnth, stid)
    res = androidselectall(qry, val)

    return jsonify(res)

@app.route('/view_attendance_staff',methods=['post'])
def view_attendance_staff():
    sid=request.form['sid']
    mnth=request.form['mnth']
    print(request.form)
    if mnth=='january':
        mnth=1
    elif mnth=='february':
        mnth=2
    elif mnth=='march':
        mnth=3
    elif mnth=='april':
        mnth=4
    elif mnth=='may':
        mnth=5
    elif mnth=='june':
        mnth=6
    elif mnth=='july':
        mnth=7
    elif mnth=='august':
        mnth=8
    elif mnth=='september':
        mnth=9
    elif mnth=='october':
        mnth=10
    elif mnth=='november':
        mnth=11
    elif mnth=='december':
        mnth=12

    qry="SELECT count(`attendance`) as twh,sum(`attendance`) as tph,(sum(`attendance`)/count(`attendance`))*100 as pe,`student`.* FROM `attendance` JOIN `student` ON `student`.`student_lid`=`attendance`.`student_id` WHERE MONTH(DATE)=%s AND `subject_id`=%s GROUP BY student_id"
    val=(mnth,sid)
    res=androidselectall(qry,val)
    print(res)
    return jsonify(res)

@app.route('/marked_attendance_staff',methods=['post'])
def marked_attendance_staff():
    ssid=request.form["ssid"]
    h=request.form["h"]
    qry="SELECT `attendance`.*,`student`.* FROM `attendance` JOIN `student`  ON `attendance`.`student_id`=`student`.`student_lid` WHERE `attendance`.`subject_id`=%s AND `attendance`.`hour`=%s AND `attendance`.`date`=CURDATE()"
    val=(ssid,h)
    res=androidselectall(qry,val)


    return jsonify(res)


@app.route('/mark_attendance',methods=['get'])
def mark_attendance():
    sid=request.args.get("sid")
    h=request.args.get("h")
    qry="SELECT `student`.* FROM `student` JOIN `subject` ON `student`.`semester`=`subject`.`semester` WHERE `subject_id`=%s"
    res=selectall(qry,sid)

    return render_template("Add attendance.html",sid=sid,val=res,h=h)

@app.route('/insertatt',methods=['post'])
def insertatt():
    sid=request.form["sid"]
    h=request.form["h"]
    att=request.form.getlist("checkbox")
    print(request.form)

    print(att)
    qry = "SELECT `student`.* FROM `student` JOIN `subject` ON `student`.`semester`=`subject`.`semester` WHERE `subject_id`=%s"
    res = selectall(qry, sid)
    print(res,"++++++++++++++++++++++++++++++++")
    attt=[]
    try:
        for i in att:
            attt.append(i)
    except:
        pass
    print(attt,"=================")
    for i in res:
        if str(i[1]) in attt:
            qry="INSERT INTO `attendance` VALUES(NULL,%s,%s,1,CURDATE(),%s)"
            val=(i[1],sid,h)
            iud(qry,val)
        else:
            qry = "INSERT INTO `attendance` VALUES(NULL,%s,%s,0,CURDATE(),%s)"
            val = (i[1], sid,h)
            iud(qry, val)
    return render_template("Added succesfully.html")


@app.route('/view_mark_student',methods=['post'])
def view_mark_student():
    stid=request.form['stid']
    print(stid)
    sem = request.form['sem']
    qry="SELECT AVG(mark) AS mark,`subject`.* FROM `mark` JOIN `subject` ON `mark`.`subject_id`=`subject`.`subject_id` WHERE `student_id`=%s AND `subject`.`semester`=%s"
    val=(stid,sem)
    res=androidselectall(qry,val)

    return jsonify(res)


@app.route('/view_work_student',methods=['post'])
def view_work_student():
    print(request.form)
    stid=request.form['subject']

    qry="SELECT * FROM `work` where Subject_id=%s"
    res=androidselectall(qry,stid)
    return jsonify(res)



@app.route('/view_workr_student',methods=['post'])
def view_workr_student():
    print(request.form)
    stid=request.form['lid']
    wid=request.form['wid']
    qry="SELECT * FROM `workreport` WHERE `student_id`=%s AND`work_id`=%s"
    val=(stid,wid)
    res=androidselectall(qry,val)
    print(res)
    return jsonify(res)




@app.route('/view_notification',methods=['post'])
def view_notification():
    qry="SELECT * FROM `notification`"
    res=androidselectallnew(qry)
    return jsonify(res)


@app.route('/view_timetable',methods=['post'])
def view_timetable():
    sem=request.form['sem']
    qry="SELECT * FROM `timetable` WHERE `sem`=%s"
    res=androidselectall(qry,sem)
    return jsonify(res)


@app.route('/view_timetable_student',methods=['post'])
def view_timetable_student():
    lid=request.form['lid']
    qry="SELECT `timetable`.* FROM student JOIN timetable ON student.semester=timetable.sem WHERE student.student_lid=%s"
    val=(lid)
    res=androidselectall(qry,val)
    return jsonify(res)


@app.route('/view_attendance_parent',methods=['post'])
def view_attendance_parent():

    stid=request.form['pid']
    mnth = request.form['mnth']
    if mnth == 'january':
        mnth = 1
    elif mnth == 'february':
        mnth = 2
    elif mnth == 'march':
        mnth = 3
    elif mnth == 'april':
        mnth = 4
    elif mnth == 'may':
        mnth = 5
    elif mnth == 'june':
        mnth = 6
    elif mnth == 'july':
        mnth = 7
    elif mnth == 'august':
        mnth = 8
    elif mnth == 'september':
        mnth = 9
    elif mnth == 'october':
        mnth = 10
    elif mnth == 'november':
        mnth = 11
    elif mnth == 'december':
        mnth = 12
    qry=" SELECT COUNT(`attendance`) AS twh,SUM(`attendance`) AS tph,(SUM(`attendance`)/COUNT(`attendance`))*100 AS pe,(COUNT(`attendance`)-SUM(`attendance`)) AS ah ,`student`.* FROM `attendance` JOIN `student` ON `student`.`student_lid`=`attendance`.`student_id` JOIN `parent` ON `parent`.`student_id`=`student`.`student_lid`  WHERE MONTH(DATE)=%s AND `parent`.`parent_lid`=%s  GROUP BY DATE"

    val=(mnth,stid)
    res=androidselectall(qry,val)

    return jsonify(res)




@app.route('/view_mark_parent',methods=['post'])
def view_mark_parent():
    stid=request.form['pid']
    print(stid)
    sem=request.form['sem']
    qry="SELECT AVG(mark) AS mark,`subject`.* FROM `mark` JOIN `subject` ON `mark`.`subject_id`=`subject`.`subject_id` JOIN `parent` ON `parent`.`student_id`=`mark`.`student_id` WHERE `parent`.`parent_lid`=%s AND `subject`.`semester`=%s"
    val=(stid,sem)
    res=androidselectall(qry,val)

    return jsonify(res)

@app.route('/view_mark_staff',methods=['post'])
def view_mark_staff():
    sid=request.form['sid']
    qry="SELECT `student`.*,AVG(mark) AS mark FROM `student` JOIN `mark` ON `student`.`student_lid`=`mark`.`student_id` WHERE `mark`.`subject_id`=%s GROUP BY student_id"
    res=androidselectall(qry,sid)

    return jsonify(res)

@app.route('/view_notification_parent',methods=['post'])
def view_notification_parent():
    qry="SELECT * FROM `notification`"
    res=androidselectallnew(qry)
    return jsonify(res)

@app.route('/deletework',methods=['post'])
def deletework():
    wid=request.form['wid']
    print(wid,"===")
    qry="DELETE FROM `work` WHERE `work_id`=%s"
    iud(qry,wid)
    return jsonify({'task':'success'})

@app.route('/deleteworkreport',methods=['post'])
def deleteworkreport():

    wid=request.form['wid']
    print(wid,"===")
    qry="DELETE FROM `workreport` WHERE `work_rid`=%s"
    iud(qry,wid)
    return jsonify({'task':'success'})


@app.route('/absentnotif',methods=['post'])
def absentnotif():
    pid=request.form['pid']
    qry="SELECT * FROM `attendance` JOIN `parent` ON `parent`.`student_id`=`attendance`.`student_id`  WHERE attendance=0  AND `attendance`.`date`=CURDATE() AND `parent`.`parent_lid`=%s"
    res=androidselectall(qry,pid)
    print(res)
    return jsonify(res)








app.run(host="0.0.0.0",port=5000)






