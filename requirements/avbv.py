"""(弃用算法)
XOR = 177451812
ADD = 100618342136696320
TABLE = "fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF"
MAP = {
    0:9,
    1:8,
    2:1,
    3:6,
    4:2,
    5:4,
    6:0,
    7:7,
    8:3,
    9:5
}
def av2bv(av):
    av = (av ^ XOR) + ADD
    bv = [""]*10
    for i in range(10):
        bv[MAP[i]] = TABLE[(av//58**i)%58]
    return "".join(bv)

def bv2av(bv):
    av = [""]*10
    s = 0
    for i in range(10):
        s += TABLE.find(bv[MAP[i]])*58**i
    av=(s-ADD)^XOR
    return(av)

def main():
    while True:
        mod = input("1.AV2BV\n2.BV2AV\n3.Exit\n你的选择:")
        if mod == "1":
            print("BV号是: BV"+av2bv(int(input("AV号是:"))))
        elif mod == "2":
            print("AV号是 AV"+str(bv2av(input("BV号是"))))
        elif mod == "3":
            break
        else:
            print("输入错误请重新输入")"""

XOR_CODE = 23442827791579
MASK_CODE = 2251799813685247
MAX_AID = 1 << 51
ALPHABET = "FcwAPNKTMug3GV5Lj7EJnHpWsx4tb8haYeviqBz6rkCy12mUSDQX9RdoZf"
ENCODE_MAP = 8, 7, 0, 5, 1, 3, 2, 4, 6
DECODE_MAP = tuple(reversed(ENCODE_MAP))

BASE = len(ALPHABET)
PREFIX = "BV1"
PREFIX_LEN = len(PREFIX)
CODE_LEN = len(ENCODE_MAP)


def av2bv(aid: int) -> str:
    bvid = [""] * 9
    tmp = (MAX_AID | aid) ^ XOR_CODE
    for i in range(CODE_LEN):
        bvid[ENCODE_MAP[i]] = ALPHABET[tmp % BASE]
        tmp //= BASE
    return PREFIX + "".join(bvid)


def bv2av(bvid: str) -> int:
    assert bvid[:3] == PREFIX

    bvid = bvid[3:]
    tmp = 0
    for i in range(CODE_LEN):
        idx = ALPHABET.index(bvid[DECODE_MAP[i]])
        tmp = tmp * BASE + idx
    return (tmp & MASK_CODE) ^ XOR_CODE


assert av2bv(111298867365120) == "BV1L9Uoa9EUx"
assert bv2av("BV1L9Uoa9EUx") == 111298867365120

if __name__ == "__main__":
    import time

    print(
        '请运行名为“TH_Bilibili_Toolbox”的主程序，本页面将于5秒后关闭。\nPlease run the main program named "TH_Bilibili_Toolbox". This page will close in 5 seconds.'
    )
    time.sleep(5)
