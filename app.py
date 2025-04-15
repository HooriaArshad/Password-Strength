import re
import streamlit as st

st.set_page_config(page_title= "**PASSWORD STRENGTH CHECKER BY HOOR ARSHAD**" , page_icon= "🔐" , layout= "centered")

st.title("🔐 password strength checker")

st.markdown ("""
## Welcome to the ultimate password strength checker !👋
 use this simple tool to check the strenght of your password and get suggestion on how to make it stronger
                  we will give you helpful tips to create a **strong password**🔐 """)


user_name = st.text_input("Enter your user name")


password = st.text_input("Enter your password", type="password")
if user_name and password:
     st.write(f"welcome, **{user_name}** 👋 ")
     st.markdown(f" **your pasword is :** {password} ")
feedback = []

strength = 0 

if password:
    if len(password) >= 6:
        strength += 1
    else :
        feedback.append("❌ password must have  at least 6 charachters long .")


    if re.search(r"[A-Z]", password) and re.search(r"[A-Z]", password):
        strength += 1

    else :
        feedback.append("❌password should contain both upper and lower case characater:" )

                        
    if re.search(r"\d", password):
        strength += 1    

    else:
        feedback.append("❌ password should contain  at least one digit : ")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    
    else:
      feedback.append("❌password should contain  at least one special character :for example !@#") 

    if strength == 4:
        feedback.append("✅ your password is strong !🥳")
        st.progress(100)    

    elif strength == 3 :
         feedback.append("🟡 your password is medium strength . it could be stronger!😮") 
         st.progress(75)

    elif strength == 2:
         feedback.append("🔴 your password is so weak . please make it stronger !😐") 
         st.progress(50) 
    else:
        feedback.append("❌password is very weak. Improve it! 😓")
        st.progress(25)

    if feedback :
        st.markdown("## improvement suggestions")
        for tip in feedback :
            st.write(tip)     

else:
 st.info("Create password.")
