import streamlit as st
import pandas as pd
import json
from pathlib import Path
from datetime import date

st.set_page_config(page_title="Hospital Management System", page_icon="🏥", layout="wide")
DATA = Path("hospital_data")
DATA.mkdir(exist_ok=True)

def load(name):
    p = DATA / f"{name}.json"
    if p.exists():
        try: return json.loads(p.read_text(encoding="utf-8"))
        except Exception: return []
    return []

def save(name):
    (DATA / f"{name}.json").write_text(json.dumps(st.session_state[name], indent=2), encoding="utf-8")

for key in ["patients", "doctors", "appointments", "records", "bills", "medicines"]:
    if key not in st.session_state: st.session_state[key] = load(key)

st.title("🏥 Hospital Management System")
st.caption("Python + Streamlit | Student project demo")
page = st.sidebar.radio("Navigation", ["Dashboard", "Patients", "Doctors", "Appointments", "Medical Records", "Billing", "Pharmacy", "Reports"])
st.sidebar.warning("Demo only: do not enter real patient data.")

patients = st.session_state.patients
doctors = st.session_state.doctors
appointments = st.session_state.appointments
records = st.session_state.records
bills = st.session_state.bills
medicines = st.session_state.medicines

def table(data, message):
    if data: st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
    else: st.info(message)

if page == "Dashboard":
    st.subheader("Dashboard Overview")
    a,b,c,d = st.columns(4)
    a.metric("Patients", len(patients)); b.metric("Doctors", len(doctors))
    c.metric("Appointments", len(appointments)); d.metric("Bills", len(bills))
    st.markdown("Use the sidebar to manage patient details, doctors, appointments, medical records, billing, pharmacy stock and reports.")

elif page == "Patients":
    st.subheader("Patient Management")
    with st.form("pform", clear_on_submit=True):
        name=st.text_input("Patient name *"); age=st.number_input("Age",0,120,18)
        gender=st.selectbox("Gender",["Not specified","Female","Male","Other"])
        contact=st.text_input("Contact (optional)"); condition=st.text_input("Reason for visit / condition")
        ok=st.form_submit_button("Add Patient")
    if ok:
        if name.strip():
            patients.append({"ID":f"P{len(patients)+1:04}","Name":name.strip(),"Age":age,"Gender":gender,"Contact":contact,"Condition":condition})
            save("patients"); st.success("Patient added."); st.rerun()
        else: st.error("Patient name is required.")
    q=st.text_input("Search by patient name or ID")
    table([x for x in patients if q.lower() in x["Name"].lower() or q.lower() in x["ID"].lower()], "No patients yet.")
    if patients:
        pid=st.selectbox("Patient to delete",["Select"]+[x["ID"] for x in patients])
        if st.button("Delete patient") and pid!="Select":
            st.session_state.patients=[x for x in patients if x["ID"]!=pid]; save("patients"); st.rerun()

elif page == "Doctors":
    st.subheader("Doctor Management")
    with st.form("dform", clear_on_submit=True):
        name=st.text_input("Doctor name *"); spec=st.text_input("Specialization"); contact=st.text_input("Contact")
        ok=st.form_submit_button("Add Doctor")
    if ok:
        if name.strip():
            doctors.append({"ID":f"D{len(doctors)+1:04}","Name":name.strip(),"Specialization":spec,"Contact":contact})
            save("doctors"); st.success("Doctor added."); st.rerun()
        else: st.error("Doctor name is required.")
    table(doctors,"No doctors yet.")
    if doctors:
        did=st.selectbox("Doctor to delete",["Select"]+[x["ID"] for x in doctors])
        if st.button("Delete doctor") and did!="Select":
            st.session_state.doctors=[x for x in doctors if x["ID"]!=did]; save("doctors"); st.rerun()

elif page == "Appointments":
    st.subheader("Appointment Management")
    pnames=[x["Name"] for x in patients]; dnames=[x["Name"] for x in doctors]
    with st.form("aform", clear_on_submit=True):
        p=st.selectbox("Patient",pnames) if pnames else st.text_input("Patient name")
        d=st.selectbox("Doctor",dnames) if dnames else st.text_input("Doctor name")
        dt=st.date_input("Appointment date",date.today()); notes=st.text_input("Notes")
        ok=st.form_submit_button("Book appointment")
    if ok:
        if str(p).strip() and str(d).strip():
            appointments.append({"ID":f"A{len(appointments)+1:04}","Patient":p,"Doctor":d,"Date":str(dt),"Notes":notes})
            save("appointments"); st.success("Appointment booked."); st.rerun()
        else: st.error("Enter patient and doctor.")
    table(appointments,"No appointments yet.")
    if appointments:
        aid=st.selectbox("Appointment to cancel",["Select"]+[x["ID"] for x in appointments])
        if st.button("Cancel appointment") and aid!="Select":
            st.session_state.appointments=[x for x in appointments if x["ID"]!=aid]; save("appointments"); st.rerun()

elif page == "Medical Records":
    st.subheader("Medical Records")
    with st.form("rform",clear_on_submit=True):
        p=st.text_input("Patient name *"); dt=st.date_input("Record date",date.today()); detail=st.text_area("Record notes *")
        ok=st.form_submit_button("Save record")
    if ok:
        if p.strip() and detail.strip():
            records.append({"ID":f"R{len(records)+1:04}","Patient":p,"Date":str(dt),"Notes":detail})
            save("records"); st.success("Record saved."); st.rerun()
        else: st.error("Patient name and notes are required.")
    table(records,"No medical records yet.")

elif page == "Billing":
    st.subheader("Billing")
    with st.form("bform",clear_on_submit=True):
        p=st.text_input("Patient name *"); consult=st.number_input("Consultation fee ₹",min_value=0.0,step=100.0)
        meds=st.number_input("Medicine charges ₹",min_value=0.0,step=50.0); other=st.number_input("Other charges ₹",min_value=0.0,step=50.0)
        ok=st.form_submit_button("Generate bill")
    if ok:
        if p.strip():
            bills.append({"Bill ID":f"B{len(bills)+1:04}","Patient":p,"Consultation":consult,"Medicine":meds,"Other":other,"Total":consult+meds+other,"Status":"Unpaid"})
            save("bills"); st.success("Bill generated."); st.rerun()
        else: st.error("Patient name is required.")
    table(bills,"No bills yet.")
    st.metric("Total billed",f"₹{sum(float(x['Total']) for x in bills):,.2f}")
    if bills:
        bid=st.selectbox("Bill to mark paid",["Select"]+[x["Bill ID"] for x in bills])
        if st.button("Mark bill paid") and bid!="Select":
            for x in bills:
                if x["Bill ID"]==bid: x["Status"]="Paid"
            save("bills"); st.rerun()

elif page == "Pharmacy":
    st.subheader("Pharmacy / Medicine Stock")
    with st.form("mform",clear_on_submit=True):
        name=st.text_input("Medicine name *"); qty=st.number_input("Quantity",min_value=0,step=1); price=st.number_input("Unit price ₹",min_value=0.0)
        ok=st.form_submit_button("Add medicine")
    if ok:
        if name.strip():
            medicines.append({"ID":f"M{len(medicines)+1:04}","Medicine":name,"Quantity":qty,"Unit price":price})
            save("medicines"); st.success("Medicine added."); st.rerun()
        else: st.error("Medicine name is required.")
    table(medicines,"No medicines yet.")
    if medicines:
        mid=st.selectbox("Medicine to update",["Select"]+[x["ID"] for x in medicines])
        delta=st.number_input("Stock change (negative to remove)",value=0,step=1)
        if st.button("Update stock") and mid!="Select":
            item=next(x for x in medicines if x["ID"]==mid)
            if item["Quantity"]+delta < 0: st.error("Stock cannot be negative.")
            else:
                item["Quantity"]+=delta; save("medicines"); st.rerun()

elif page == "Reports":
    st.subheader("Reports & Export")
    c1,c2,c3=st.columns(3); c1.metric("Patients",len(patients)); c2.metric("Doctors",len(doctors)); c3.metric("Appointments",len(appointments))
    st.metric("Total billed",f"₹{sum(float(x['Total']) for x in bills):,.2f}")
    payload={"patients":patients,"doctors":doctors,"appointments":appointments,"records":records,"bills":bills,"medicines":medicines}
    st.download_button("Download all data (JSON)",json.dumps(payload,indent=2),file_name="hospital_report.json",mime="application/json")
    for title,data in [("Patients",patients),("Doctors",doctors),("Appointments",appointments),("Medical Records",records),("Bills",bills),("Medicines",medicines)]:
        if data: st.download_button(f"Download {title} CSV",pd.DataFrame(data).to_csv(index=False),file_name=title.lower().replace(" ","_")+".csv",mime="text/csv",key=title)

st.divider()
st.caption("Student demonstration project; not designed for real clinical use.")
