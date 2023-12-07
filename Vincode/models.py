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
    
    類型 = models.CharField(("類型"),max_length=50, null=True)  
    車種 = models.CharField("車種",max_length=50, null=True)  
    VIN = models.CharField("VIN",max_length=50, null=True)  
    中文等級 = models.CharField("中文等級",max_length=50, null=True)  
    出廠年月 = models.CharField("出廠年月",max_length=50, null=True)  
    排氣量_x = models.CharField("排氣量_x",max_length=50, null=True)  
    車身型式 = models.CharField("車身型式",max_length=50, null=True)  
    車重 = models.CharField("車重",max_length=50, null=True)  
    價格_x = models.CharField("價格_x",max_length=50, null=True)  
    車牌號碼 = models.CharField("車牌號碼",max_length=50, null=True) 
    CARMDL = models.CharField("CARMDL",max_length=50, null=True)
    SFX = models.CharField("SFX",max_length=50, null=True) 
    價格_y = models.CharField("價格_y",max_length=50, null=True)  
    車身座位 = models.CharField("車身座位",max_length=50, null=True)  
    變速系統 = models.CharField("變速系統",max_length=50, null=True)  
    動力型式 = models.CharField("動力型式",max_length=50, null=True)  
    定速巡航 = models.CharField("定速巡航",max_length=50, null=True)  
    蜂鳴式倒車輔助系統 = models.CharField("蜂鳴式倒車輔助系統",max_length=50, null=True)  
    倒車影像輔助 = models.CharField("倒車影像輔助",max_length=50, null=True)  
    前方駐車雷達 = models.CharField("前方駐車雷達",max_length=50, null=True)  
    循跡防滑控制系統 = models.CharField("循跡防滑控制系統",max_length=50, null=True)  
    車道偏離警示系統 = models.CharField("車道偏離警示系統",max_length=50, null=True)  
    車道變換輔助系統 = models.CharField("車道變換輔助系統",max_length=50, null=True)  
    ACC主動跟車系統 = models.CharField("ACC主動跟車系統",max_length=50, null=True)  
    車道維持輔助系統 = models.CharField("車道維持輔助系統",max_length=50, null=True)  
    AEB自動緊急煞車系統 = models.CharField("AEB自動緊急煞車系統",max_length=50, null=True)  
    電子煞車力分配系統 = models.CharField("電子煞車力分配系統",max_length=50, null=True)  
    EBS = models.CharField("EBS",max_length=50, null=True)  
    雷達碰撞預防系統 = models.CharField("雷達碰撞預防系統",max_length=50, null=True)  
    自動停車系統 = models.CharField("自動停車系統",max_length=50, null=True)  
    雙前座正面氣囊 = models.CharField("雙前座正面氣囊",max_length=50, null=True)  
    雙前座側面氣囊 = models.CharField("雙前座側面氣囊",max_length=50, null=True)  
    前座中央防碰撞氣囊 = models.CharField("前座中央防碰撞氣囊",max_length=50, null=True)  
    右前座膝部氣囊 = models.CharField("右前座膝部氣囊",max_length=50, null=True)  
    右前座正面氣囊 = models.CharField("右前座正面氣囊",max_length=50, null=True)  
    後座側面氣囊 = models.CharField("後座側面氣囊",max_length=50, null=True)  
    駕駛座正面氣囊 = models.CharField("駕駛座正面氣囊",max_length=50, null=True) 
    駕駛座膝部氣囊 = models.CharField("駕駛座膝部氣囊",max_length=50, null=True)  
    雙前座膝部氣囊 = models.CharField("雙前座膝部氣囊",max_length=50, null=True)  
    左後座腿靠氣囊 = models.CharField("左後座腿靠氣囊",max_length=50, null=True)  
    右後座防潛滑氣囊 = models.CharField("右後座防潛滑氣囊",max_length=50, null=True)  
    右後座腿靠氣囊 = models.CharField("右後座腿靠氣囊",max_length=50, null=True) 
    
    def __str__(self):
        return self.name
    
    # 使用實際存在的欄位名稱
    class Meta:
        ordering = ['類型', '車種', 'VIN', '中文等級','出廠年月','排氣量_x','車身型式','車重','價格_x','車牌號碼','CARMDL','SFX','價格_y','車身座位',
                    '變速系統','動力型式','定速巡航','蜂鳴式倒車輔助系統','倒車影像輔助','前方駐車雷達','循跡防滑控制系統','車道偏離警示系統',
                    '車道變換輔助系統','ACC主動跟車系統','車道維持輔助系統','AEB自動緊急煞車系統','電子煞車力分配系統','EBS','雷達碰撞預防系統',
                    '自動停車系統','雙前座正面氣囊','雙前座側面氣囊','前座中央防碰撞氣囊','右前座膝部氣囊','右前座正面氣囊','後座側面氣囊','駕駛座正面氣囊',
                    '駕駛座膝部氣囊','雙前座膝部氣囊','左後座腿靠氣囊','右後座防潛滑氣囊','右後座腿靠氣囊']


from django.utils import timezone

timezone.now
