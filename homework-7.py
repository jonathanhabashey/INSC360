import xml.etree.ElementTree as ET

tree = ET.parse("hw7.xml")
root = tree.getroot()
student_node = root.findall("student")
for student in student_node:
    studentName = student.find("name").text
    studentMajor = student.find("major").text
    studentMinor = student.find("minor")
    if studentMinor != None:
        studentMinorString = studentMinor.text
    else:
        studentMinorString = "N/A"
    studentDate = student.find("gradyear").text
    print("Student: ", studentName, "Major: ", studentMajor, "Minor: ", studentMinorString, "Grad Year: ",
          studentDate)



