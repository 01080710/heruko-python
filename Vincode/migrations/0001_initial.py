# Generated by Django 4.2.7 on 2024-01-25 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CombineLexus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("類型", models.CharField(max_length=255, null=True, verbose_name="類型")),
                ("車種", models.CharField(max_length=255, null=True, verbose_name="車種")),
                (
                    "CARMDL",
                    models.CharField(max_length=255, null=True, verbose_name="CARMDL"),
                ),
                (
                    "SFX",
                    models.CharField(max_length=255, null=True, verbose_name="SFX"),
                ),
                (
                    "出廠年月",
                    models.CharField(max_length=255, null=True, verbose_name="出廠年月"),
                ),
                ("年份", models.CharField(max_length=255, null=True, verbose_name="年份")),
                (
                    "WMI",
                    models.CharField(max_length=255, null=True, verbose_name="WMI"),
                ),
                (
                    "VDS",
                    models.CharField(max_length=255, null=True, verbose_name="VDS"),
                ),
                (
                    "VALADATION",
                    models.CharField(
                        max_length=255, null=True, verbose_name="VALADATION"
                    ),
                ),
                (
                    "VIS_min",
                    models.CharField(max_length=255, null=True, verbose_name="VIS_min"),
                ),
                (
                    "VIS_max",
                    models.CharField(max_length=255, null=True, verbose_name="VIS_max"),
                ),
                (
                    "match",
                    models.CharField(max_length=255, null=True, verbose_name="match"),
                ),
                (
                    "車身碼",
                    models.CharField(max_length=255, null=True, verbose_name="車身碼"),
                ),
                (
                    "中文等級",
                    models.CharField(max_length=255, null=True, verbose_name="中文等級"),
                ),
                (
                    "排氣量",
                    models.CharField(max_length=255, null=True, verbose_name="排氣量"),
                ),
                ("價格", models.CharField(max_length=255, null=True, verbose_name="價格")),
                (
                    "估價日期",
                    models.CharField(max_length=255, null=True, verbose_name="估價日期"),
                ),
                (
                    "保險到期日",
                    models.CharField(max_length=255, null=True, verbose_name="保險到期日"),
                ),
                (
                    "銷售日",
                    models.CharField(max_length=255, null=True, verbose_name="銷售日"),
                ),
                (
                    "統計代碼",
                    models.CharField(max_length=255, null=True, verbose_name="統計代碼"),
                ),
                (
                    "限乘人數",
                    models.CharField(max_length=255, null=True, verbose_name="限乘人數"),
                ),
                (
                    "Label",
                    models.CharField(max_length=255, null=True, verbose_name="Label"),
                ),
                (
                    "車身座位",
                    models.CharField(max_length=255, null=True, verbose_name="車身座位"),
                ),
                (
                    "變速系統",
                    models.CharField(max_length=255, null=True, verbose_name="變速系統"),
                ),
                (
                    "動力型式",
                    models.CharField(max_length=255, null=True, verbose_name="動力型式"),
                ),
                (
                    "車身型式",
                    models.CharField(max_length=255, null=True, verbose_name="車身型式"),
                ),
                ("車重", models.CharField(max_length=255, null=True, verbose_name="車重")),
                (
                    "定速巡航",
                    models.CharField(max_length=255, null=True, verbose_name="定速巡航"),
                ),
                (
                    "蜂鳴式倒車輔助系統",
                    models.CharField(
                        max_length=255, null=True, verbose_name="蜂鳴式倒車輔助系統"
                    ),
                ),
                (
                    "倒車影像輔助",
                    models.CharField(max_length=255, null=True, verbose_name="倒車影像輔助"),
                ),
                (
                    "前方駐車雷達",
                    models.CharField(max_length=255, null=True, verbose_name="前方駐車雷達"),
                ),
                (
                    "循跡防滑控制系統",
                    models.CharField(
                        max_length=255, null=True, verbose_name="循跡防滑控制系統"
                    ),
                ),
                (
                    "車道偏離警示系統",
                    models.CharField(
                        max_length=255, null=True, verbose_name="車道偏離警示系統"
                    ),
                ),
                (
                    "車道變換輔助系統",
                    models.CharField(
                        max_length=255, null=True, verbose_name="車道變換輔助系統"
                    ),
                ),
                (
                    "ACC主動跟車系統",
                    models.CharField(
                        max_length=255, null=True, verbose_name="ACC主動跟車系統"
                    ),
                ),
                (
                    "車道維持輔助系統",
                    models.CharField(
                        max_length=255, null=True, verbose_name="車道維持輔助系統"
                    ),
                ),
                (
                    "AEB自動緊急煞車系統",
                    models.CharField(
                        max_length=255, null=True, verbose_name="AEB自動緊急煞車系統"
                    ),
                ),
                (
                    "電子煞車力分配系統",
                    models.CharField(
                        max_length=255, null=True, verbose_name="電子煞車力分配系統"
                    ),
                ),
                (
                    "EBS",
                    models.CharField(max_length=255, null=True, verbose_name="EBS"),
                ),
                (
                    "雷達碰撞預防系統",
                    models.CharField(
                        max_length=255, null=True, verbose_name="雷達碰撞預防系統"
                    ),
                ),
                (
                    "自動停車系統",
                    models.CharField(max_length=255, null=True, verbose_name="自動停車系統"),
                ),
                (
                    "雙前座正面氣囊",
                    models.CharField(max_length=255, null=True, verbose_name="雙前座正面氣囊"),
                ),
                (
                    "雙前座側面氣囊",
                    models.CharField(max_length=255, null=True, verbose_name="雙前座側面氣囊"),
                ),
                (
                    "前座中央防碰撞氣囊",
                    models.CharField(
                        max_length=255, null=True, verbose_name="前座中央防碰撞氣囊"
                    ),
                ),
                (
                    "右前座膝部氣囊",
                    models.CharField(max_length=255, null=True, verbose_name="右前座膝部氣囊"),
                ),
                (
                    "右前座正面氣囊",
                    models.CharField(max_length=255, null=True, verbose_name="右前座正面氣囊"),
                ),
                (
                    "後座側面氣囊",
                    models.CharField(max_length=255, null=True, verbose_name="後座側面氣囊"),
                ),
                (
                    "駕駛座正面氣囊",
                    models.CharField(max_length=255, null=True, verbose_name="駕駛座正面氣囊"),
                ),
                (
                    "駕駛座膝部氣囊",
                    models.CharField(max_length=255, null=True, verbose_name="駕駛座膝部氣囊"),
                ),
                (
                    "雙前座膝部氣囊",
                    models.CharField(max_length=255, null=True, verbose_name="雙前座膝部氣囊"),
                ),
                (
                    "左後座腿靠氣囊",
                    models.CharField(max_length=255, null=True, verbose_name="左後座腿靠氣囊"),
                ),
                (
                    "右後座防潛滑氣囊",
                    models.CharField(
                        max_length=255, null=True, verbose_name="右後座防潛滑氣囊"
                    ),
                ),
                (
                    "右後座腿靠氣囊",
                    models.CharField(max_length=255, null=True, verbose_name="右後座腿靠氣囊"),
                ),
                (
                    "VIS_min_false",
                    models.CharField(
                        max_length=255, null=True, verbose_name="VIS_min_false"
                    ),
                ),
                (
                    "VIS_max_false",
                    models.CharField(
                        max_length=255, null=True, verbose_name="VIS_max_false"
                    ),
                ),
            ],
            options={
                "ordering": [
                    "類型",
                    "車種",
                    "CARMDL",
                    "SFX",
                    "出廠年月",
                    "年份",
                    "WMI",
                    "VDS",
                    "VALADATION",
                    "VIS_min",
                    "VIS_max",
                    "match",
                    "車身碼",
                    "中文等級",
                    "排氣量",
                    "價格",
                    "估價日期",
                    "保險到期日",
                    "銷售日",
                    "統計代碼",
                    "限乘人數",
                    "Label",
                    "車身座位",
                    "變速系統",
                    "動力型式",
                    "車身型式",
                    "車重",
                    "定速巡航",
                    "蜂鳴式倒車輔助系統",
                    "倒車影像輔助",
                    "前方駐車雷達",
                    "循跡防滑控制系統",
                    "車道偏離警示系統",
                    "車道變換輔助系統",
                    "ACC主動跟車系統",
                    "車道維持輔助系統",
                    "AEB自動緊急煞車系統",
                    "電子煞車力分配系統",
                    "EBS",
                    "雷達碰撞預防系統",
                    "自動停車系統",
                    "雙前座正面氣囊",
                    "雙前座側面氣囊",
                    "前座中央防碰撞氣囊",
                    "右前座膝部氣囊",
                    "右前座正面氣囊",
                    "後座側面氣囊",
                    "駕駛座正面氣囊",
                    "駕駛座膝部氣囊",
                    "雙前座膝部氣囊",
                    "左後座腿靠氣囊",
                    "右後座防潛滑氣囊",
                    "右後座腿靠氣囊",
                    "VIS_min_false",
                    "VIS_max_false",
                ],
            },
        ),
        migrations.CreateModel(
            name="MyModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=300)),
                ("complete", models.BooleanField()),
                (
                    "todolist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Vincode.mymodel",
                    ),
                ),
            ],
        ),
    ]
