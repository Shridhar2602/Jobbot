import WebCode.lenoxex as website1
import WebCode.newagesys as website2
import build.gui as GUI

GUI.Start()

info = GUI.info
resume_path = GUI.filepath

print(info)
print(resume_path)

website1.web(info, resume_path)
website2.web(info, resume_path)

# scrap.begin()