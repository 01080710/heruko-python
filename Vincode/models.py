from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
class Item(models.Model):
    todolist = models.ForeignKey(MyModel,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
    
class CombineLexus(models.Model):
    
    類型 = models.CharField("類型",max_length=255, null=True)  
    車種 = models.CharField("車種",max_length=255, null=True)  
    CARMDL = models.CharField("CARMDL",max_length=255, null=True)  
    SFX = models.CharField("SFX",max_length=255, null=True)  
    出廠年月 = models.CharField("出廠年月",max_length=255, null=True)  
    年份 = models.CharField("年份",max_length=255, null=True)  
    WMI = models.CharField("WMI",max_length=255, null=True)  
    VDS = models.CharField("VDS",max_length=255, null=True)  
    VALADATION = models.CharField("VALADATION",max_length=255, null=True)  
    VIS_min = models.CharField("VIS_min",max_length=255, null=True) 
    VIS_max = models.CharField("VIS_max",max_length=255, null=True)
    match = models.CharField("match",max_length=255, null=True) 
    車身碼 = models.CharField("車身碼",max_length=255, null=True)  
    中文等級 = models.CharField("中文等級",max_length=255, null=True)  
    排氣量 = models.CharField("排氣量",max_length=255, null=True)  
    價格 = models.CharField("價格",max_length=255, null=True) 
    估價日期 = models.CharField("估價日期",max_length=255, null=True)  
    保險到期日 = models.CharField("保險到期日",max_length=255, null=True)  
    銷售日 = models.CharField("銷售日",max_length=255, null=True) 
    統計代碼 = models.CharField("統計代碼",max_length=255, null=True) 
    限乘人數 = models.CharField("限乘人數",max_length=255, null=True)  
    Label = models.CharField("Label",max_length=255, null=True)  
    車身座位 = models.CharField("車身座位",max_length=255, null=True) 
    變速系統 = models.CharField("變速系統",max_length=255, null=True)  
    動力型式 = models.CharField("動力型式",max_length=255, null=True)  
    車身型式 = models.CharField("車身型式",max_length=255, null=True)  
    車重 = models.CharField("車重",max_length=255, null=True)  
    定速巡航 = models.CharField("定速巡航",max_length=255, null=True)  
    蜂鳴式倒車輔助系統 = models.CharField("蜂鳴式倒車輔助系統",max_length=255, null=True)  
    倒車影像輔助 = models.CharField("倒車影像輔助",max_length=255, null=True)  
    前方駐車雷達 = models.CharField("前方駐車雷達",max_length=255, null=True)  
    循跡防滑控制系統 = models.CharField("循跡防滑控制系統",max_length=255, null=True)  
    車道偏離警示系統 = models.CharField("車道偏離警示系統",max_length=255, null=True)  
    車道變換輔助系統 = models.CharField("車道變換輔助系統",max_length=255, null=True)  
    ACC主動跟車系統 = models.CharField("ACC主動跟車系統",max_length=255, null=True)  
    車道維持輔助系統 = models.CharField("車道維持輔助系統",max_length=255, null=True)  
    AEB自動緊急煞車系統 = models.CharField("AEB自動緊急煞車系統",max_length=255, null=True)  
    電子煞車力分配系統 = models.CharField("電子煞車力分配系統",max_length=255, null=True)  
    EBS = models.CharField("EBS",max_length=255, null=True)  
    雷達碰撞預防系統 = models.CharField("雷達碰撞預防系統",max_length=255, null=True)  
    自動停車系統 = models.CharField("自動停車系統",max_length=255, null=True)  
    雙前座正面氣囊 = models.CharField("雙前座正面氣囊",max_length=255, null=True)  
    雙前座側面氣囊 = models.CharField("雙前座側面氣囊",max_length=255, null=True)  
    前座中央防碰撞氣囊 = models.CharField("前座中央防碰撞氣囊",max_length=255, null=True)  
    右前座膝部氣囊 = models.CharField("右前座膝部氣囊",max_length=255, null=True)  
    右前座正面氣囊 = models.CharField("右前座正面氣囊",max_length=255, null=True)  
    後座側面氣囊 = models.CharField("後座側面氣囊",max_length=255, null=True)  
    駕駛座正面氣囊 = models.CharField("駕駛座正面氣囊",max_length=255, null=True) 
    駕駛座膝部氣囊 = models.CharField("駕駛座膝部氣囊",max_length=255, null=True)  
    雙前座膝部氣囊 = models.CharField("雙前座膝部氣囊",max_length=255, null=True)  
    左後座腿靠氣囊 = models.CharField("左後座腿靠氣囊",max_length=255, null=True)  
    右後座防潛滑氣囊 = models.CharField("右後座防潛滑氣囊",max_length=255, null=True)  
    右後座腿靠氣囊 = models.CharField("右後座腿靠氣囊",max_length=255, null=True) 
    VIS_min_false = models.CharField("VIS_min_false",max_length=255, null=True) 
    VIS_max_false = models.CharField("VIS_max_false",max_length=255, null=True) 
    #VIS_min_false = models.TextField("VIS_min_false", null=True)
    #VIS_max_false = models.TextField("VIS_max_false", null=True)
    
    def __str__(self):
        return self.name
    

    
    # 使用實際存在的欄位名稱
    class Meta:
        ordering = ['類型', '車種', 'CARMDL', 'SFX','出廠年月','年份','WMI','VDS','VALADATION','VIS_min','VIS_max','match','車身碼','中文等級',
                    '排氣量','價格','估價日期','保險到期日','銷售日','統計代碼','限乘人數','Label','車身座位','變速系統','動力型式','車身型式','車重' ,                   
                    '定速巡航','蜂鳴式倒車輔助系統','倒車影像輔助','前方駐車雷達','循跡防滑控制系統','車道偏離警示系統','車道變換輔助系統','ACC主動跟車系統',
                    '車道維持輔助系統','AEB自動緊急煞車系統','電子煞車力分配系統','EBS','雷達碰撞預防系統','自動停車系統','雙前座正面氣囊','雙前座側面氣囊',
                    '前座中央防碰撞氣囊','右前座膝部氣囊','右前座正面氣囊','後座側面氣囊','駕駛座正面氣囊','駕駛座膝部氣囊','雙前座膝部氣囊','左後座腿靠氣囊',
                    '右後座防潛滑氣囊','右後座腿靠氣囊','VIS_min_false','VIS_max_false']






from django.utils import timezone

timezone.now
