#Main.COnfig
#Kylenath Timestamp

from flask import g
from datetime import datetime
import phonenumbers
import folium
import time
import geocoder
from flask import Flask  , url_for , render_template , request
import os , random , string 
from werkzeug.utils import secure_filename
from flask_mail import Mail , Message

app=Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] ="ekylenath@gmail.com"
app.config['MAIL_PASSWORD'] ="knathfarm254"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

UPLOAD_FOLDER = os.path.join(app.static_folder , "") + "/images/beef" 
UPLOAD_FOLDER_1= os.path.join(app.static_folder , "") + "/images/sheep" 
UPLOAD_FOLDER_2= os.path.join(app.static_folder , "") + "/images/chicken"
UPLOAD_FOLDER_3= os.path.join(app.static_folder , "") + "/images/pigs"  
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_1']=UPLOAD_FOLDER_1
app.config['UPLOAD_FOLDER_2']=UPLOAD_FOLDER_2
app.config['UPLOAD_FOLDER_3']=UPLOAD_FOLDER_3
#Global
webtitle=""

#
entuser = "kylenath_users.txt"
customer_data =  os.path.join(app.static_folder , "") + entuser
orderbox = "KylenathOrders.txt"
#GLobal

#Timestamp Function
def get_time():
    current = datetime.now()
    now_stamp =current.strftime("%H:%M:%S")
    return now_stamp


@app.route("/")
def home():
    timestamp=get_time()
    with open("webid.txt", "r") as web_block :
          webtittle=web_block.readlines()


    with open("imgserver.txt" , "a") as image:
         image_name=os.listdir(os.path.join(app.static_folder, "images/chicken/"))
         image_count=len(image_name)
         defactor=1
         
    with open("pigserver.txt" , "a") as image:
         pig_image=os.listdir(os.path.join(app.static_folder, "images/pigs/"))
         pig_count=len(pig_image)
         defactor=1

    return render_template("kylehome.html" , image_name=image_name,  timestamp=timestamp  , webtitle=webtitle , image_count=image_count ,  pig_image=pig_image , pig_count=pig_count , defactor=defactor )


@app.route("/finisher")
def finisher():
    with open("beefserver.txt" , "a") as beefimg :
           product_name= os.listdir(os.path.join(app.static_folder, "images/beef/"))


    with open("sheepserver.txt", "a") as sheepimg :
           sh_product = os.listdir(os.path.join(app.static_folder, "images/sheep/"))


    return render_template("fin.html", product_name=product_name, sh_product=sh_product)




@app.route("/transmission")
def transmission():
    return render_template("/transactiontab.html")

@app.route("/transact", methods=['POST', 'GET'])
def transact():
   
     transname=str(request.form.get("username"))
     stroke=transname + "_payment.txt"
     transdata=str(request.form.get("usertrs"))
     transfile=os.path.join(app.static_folder, "" )  + stroke 

     with open (transfile , "w" ) as transit :
         transit.write(transdata)
     return render_template("admin.html")


@app.route("/about")
def about():
    return render_template("/about.html")


@app.route('/admin' , methods=['POST' , 'GET'])
def admin():
         return render_template("admin.html")




@app.route('/upload_beef' , methods=['POST' , 'GET']) 
def upload_beef():
     
       if request.method =='POST':
        file = request.files['file']
       if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
       return render_template("admin.html")     

        
@app.route('/upload_chick' , methods=['POST' , 'GET']) 
def upload_chick():
        if request.method =='POST':
        #Chicken Upload 
           file = request.files['xfile']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER_2'],filename))
        #Pig Upload 
        return render_template("admin.html") 
        
@app.route('/upload_pig' , methods=['POST' , 'GET']) 
def upload_pig():
        file = request.files['zfile']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER_3'],filename))
        return render_template("admin.html") 
        
        #Sheep Upload 
@app.route('/upload_sheep' , methods=['POST' , 'GET']) 
def upload_sheep():
        file = request.files['yfile']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER_1'],filename))
        return render_template("admin.html") 

@app.route("/customer")
def customer():

      with open (customer_data , "r") as hotie :
          hotdata=(hotie.readlines())
          print(hotdata)

      return render_template("customer.html" , hotdata=hotdata , len=len(hotdata))


@app.route("/register")
def register():
    return render_template("/signup.html")

@app.route("/login.html")
def login():
    return render_template("/login.html")
 
 
@app.route("/identity")
def identity(): 
    return render_template("/identity.html")   
    
@app.route("/login.html/" , methods=['POST', 'GET'])
def login_hub():
            wallmsg="Unknown Login Id , Kindly Register "
            user_feed=str(request.form.get('username'))
            bunker=os.path.join(app.static_folder, "" ) + user_feed + ".txt"
            ata=open(bunker , 'r').readlines() 
            data = [ x.strip() for x  in ata]  
            print(data)
            pass_feed=request.form.get('password')
            if((user_feed == "admin")& (pass_feed == "0000")):
                # admin
                return render_template("/admin.html")
            if( (pass_feed==data[-1])):
                return render_template("kylehome.html")
                
            return render_template("login.html" , wallmsg=wallmsg)
                #Test Existence

@app.route("/order")
def order(): 
    return render_template("orderform.html")
    

@app.route("/gen_processing" , methods=["POST", "GET"])
def process():
     def rachize():
        for i in range(3):
    # get random string of length 6 without repeating letters
            result_str = ''.join(random.sample(string.ascii_lowercase, 8))
        return result_str

     def name_return(swap): 
        object=swap.index("@")
        swapper=swap[:object] 
        return swapper
        
        
     storeback= {}
     storeback = request.form
     useremail=str(request.form.get("email"))
     userid=str(request.form.get("xuserid"))
     order_location=request.form.get("location")
     order_product=str(request.form.get("county"))
     order_quantity=request.form.get("quantity")
     phonenumber=request.form.get("phonecnt")
     status=request.form.get("live")
     product=request.form.get("dropproduct")
     chops=request.form.get("chops")
     breed=request.form.get("breed")
     order_id=rachize()
     
     
     blackbox = os.path.join(app.static_folder, "" ) + orderbox + ".txt" 
     filehandler = useremail + "_ord_"
     with open(blackbox, "a") as handlepoint: 
          handlepoint.writelines(filehandler)
          handlepoint.writelines("\n")
          
          
     redbox = os.path.join(app.static_folder, "" ) + filehandler + ".txt" 
     with open(redbox , "w") as bundlepoint:
            for data in storeback.values():
             bundlepoint.writelines(data)
             bundlepoint.writelines("\n")
      
     print(storeback)
     
      #Sending The Order Email
     mailer="/mailorder"
     msg = Message('[KYLENATH ENTERPRISES ORDER]', sender = 'ekylenath@gmail.com', recipients = [useremail ])
     msg.html = render_template(mailer + ".html" , userid=userid,   useremail=useremail, order_quantity=order_quantity , order_location=order_location , order_product=order_product , phonenumber=phonenumber , product=product, chops=chops , breed=breed , order_id=order_id )
     mail.send(msg)

     return render_template("kylehome.html")
   
@app.route("/adduser" , methods=["POST", "GET"])
def adduser():
    datastore={}
    datastore=request.form
    current_mail=request.form.get("email")
    firstname=request.form.get("firstname")
    lastname=request.form.get("lastname")
    current_username=request.form.get("userid")
    current_password=request.form.get("key")
    contact=request.form.get("phone")

    mailer="/signcnf.html"
    msg=Message('[***- KYLENATH REGISTRATION MAIL -***] ', sender = 'ekylenath@gmail.com', recipients = [current_mail])
    msg.html = render_template(mailer , firstname=firstname , lastname=lastname , current_username=current_username   )
    mail.send(msg)
    
    
    filename= os.path.join(app.static_folder , "") + current_username + ".txt"
    with open(filename , "w")as object:
         for data in datastore.values():
             object.write(data)
             object.write("\n")

    userfile = os.path.join(app.static_folder , "") + entuser
    with open(userfile , "a") as appfixer :
         appfixer.writelines(firstname)

    return render_template("kylehome.html")
#Main
if __name__=='__main__':
   app.run()
