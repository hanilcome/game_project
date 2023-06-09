import random
import os
import sys
import time
import subprocess
from Color import Colors
from intro import *
from character import *


class Store():
    weapon_warrior = {
        "1": "철검(100gold)",
        "2": "단검(100gold)",
        "3": "대검(200gold)",
        "4": "모닝스타(200gold)",
        "5": "장미칼(1000gold)"
    }
    weapon_archer = {
        "1": "단궁(100gold)",
        "2": "석궁(100gold)",
        "3": "장궁(200gold)",
        "4": "발리스타(200gold)",
        "5": "엘프의 활(1000gold)"
    }
    weapon_wizard = {
        "1": "빗자루(100gold)",
        "2": "마술봉(100gold)",
        "3": "+5강 몽둥이(200gold)",
        "4": "현자의 지팡이(200gold)",
        "5": "자쿰의 나뭇가지(1000gold)"
    }
    armor_all = {
        "1": "모자(100gold)",
        "2": "상의(100gold)",
        "3": "신발(100gold)",
        "4": "장갑(200gold)",
        "5": "벨트(100gold)",
    }
    potion = {
        "1": "hp포션(100gold)",
        "2": "mp포션(100gold)"
    }

    def buy_weapon(self, dict, other):
        if dict == "철검(100gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "단검(100gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "대검(200gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "모닝스타(200gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "장미칼(1000gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "단궁(100gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "석궁(100gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "장궁(100gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "발리스타(200gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "엘프의 활(1000gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "빗자루(100gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "마술봉(100gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "+5강 몽둥이(200gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "현자의 지팡이(200gold)":
            other.power = max(other.power + 5, 0)
        elif dict == "자쿰의 나뭇가지(1000gold)":
            other.power = max(other.power + 5, 0)

    def buy_armor(self, dict, other):
        if dict == "모자(100gold)":
            other.max_hp = max(other.max_hp + 10, 0)
        elif dict == "상의(100gold)":
            other.max_hp = max(other.max_hp + 20, 0)
        elif dict == "신발(100gold)":
            other.max_hp = max(other.max_hp + 10, 0)
        elif dict == "장갑(200gold)":
            other.max_mp = max(other.max_mp + 15, 0)
        elif dict == "벨트(100gold)":
            other.max_mp = max(other.max_mp + 10, 0)
                  

    def buy_potion(self, dict, other):
        if dict == "hp포션(100gold)":
            other.hp_potion = max(other.hp_potion + 1, 0)
        if dict == "mp포션(100gold)":
            other.mp_potion = max(other.mp_potion + 1, 0)


# ================================================== Main ===========================================================
# 이름 입력코드 시작
user_name = input("\n\n\n\n\n\n\n\n이름을 입력하세요\n\n\n\n\n\n답변: ")
# 이름 입력코드 끝

# print(f"\n\n\n\n\n\n\n\n-제 이름은 {user_name} 입니다!!!\n\n\n\n\n\n")
# time.sleep(4)
# print("\n\n\n\n\n\n\n\n-오호 사실 떠돌이 깡통인 줄 알았는데 이름이 있긴 있었군!\n\n\n\n\n\n")
# time.sleep(4)
# print(f"\n\n\n\n\n\n\n\n-가만보자... {user_name}(이)라... 자축인묘진사오미....\n\n\n\n\n\n")
# time.sleep(4)
# print("\n\n\n\n\n\n\n\n-아니 이건!!!! 이건 필시 용사가 될 이름이네!!!!!!!!!!\n\n\n\n\n\n")
# time.sleep(3.5)
# print("\n\n\n\n\n\n\n\n-에? 용사요?! 갑자기?!\n\n\n\n\n\n")
# time.sleep(2)
# print("\n\n\n\n\n\n\n\n-그래!!! 자네 빨리 직업을 고르게!!!!\n\n\n\n\n\n")
# time.sleep(3)
# print("\n\n\n\n\n\n\n\n-시간이 없어!! 마왕이 탑을 세우고 그 안에서 군대를 만들고 있네!!\n\n\n\n\n\n")
# time.sleep(3.5)
# print("\n\n\n\n\n\n\n\n-마왕의 군대가 완성되면 탑에서 괴물들을 풀어 슬라임 마을을 공격할거야!\n\n\n\n\n\n")
# time.sleep(3.5)
# print("\n\n\n\n\n\n\n\n-그 전에 우리가 먼저 탑에 들어가 마왕의 군대를 망가뜨려 놓자고!\n\n\n\n\n\n")
# time.sleep(3)
# print("\n\n\n\n\n\n\n\n-아차차!!! 내 정신 좀 봐. 우선 무슨 직업이 있는지 알려주지!\n\n\n\n\n\n")
# time.sleep(4)

while (True):
    # 직업 입력코드 시작
    user_occupation = input(
        f"\033[31m[전사]\n전사는 강인한 체력과 힘을 바탕으로 용감무쌍한 공격을 펼치는 전쟁의 화신입니다.\033[0m\n\n\033[35m[주술사]\n주술사는 마력의 힘을 빌려 기상천외한 공격을 펼치는 진리의 수호자입니다.\033[0m\n\n\033[92m[궁수]\n궁수는 재빠른 몸놀림으로 치명적인 공격을 하는 일대일 전투의 베테랑입니다.\033[0m\n\n\n\n\n\n(전사/주술사/궁수 중 입력)\n답변: ")
    if (user_occupation == "전사" or user_occupation == "주술사" or user_occupation == "궁수"):
        break
    else:
        print("어허 틀렸네! 셋 중에 다시 고르게!")
        time.sleep(3)
        continue
# 직업 입력코드 끝

# time.sleep(3)
# print(
#     f"\n\n\n\n\n\n\n\n-크으!{user_name} 자네! {user_occupation}를 골랐구만 그래! 자네랑 찰떡이구만!!\n\n\n\n\n\n")
# time.sleep(3)
# print("\n\n\n\n\n\n\n\n-일단은 내 오두막으로 가지!\n\n\n\n\n\n")
# time.sleep(3)

# # 오두막 메뉴 보여주기 코드 시작
# print("\n\n\n\n======================[아저씨의 오두막]========================\n\n           1.마왕의탑       2.상점       3.가방\n\n===============================================================\n\n\n\n")
# # 오두막 메뉴 보여주기 코드 끝

# time.sleep(5)
# print(f"-자 어때! 위의 메뉴가 보이지? \n\n\033[33m오두막\033[0m에서는 이렇게 여러 메뉴를 선택할 수 있네.\n\n전투를 하고 싶다면 마왕의 탑에, 탑에서 번 돈으로 아이템을 사고 싶으면 상점에, 모아놓은 아이템을 보고 싶다면 가방에 해당하는 번호를 입력하게!\n물론 지금은 말고 튜토리얼이 후에 말이야 하하하하\n")
# time.sleep(10)
# print("\n\n\n\n\n\n\n\n-이로써 튜토리얼은 끝났네!\n\n왜 전투 연습을 안시켜주냐구?\n\n인생은 실전이야 친구!!\n\n\n\n\n\n")
# time.sleep(4)
# print("\n\n\n\n\n\n\n\n하하하하하하하하\n\n\n\n\n\n")
# time.sleep(1)
# print("\n\n\n\n\n\n\n\n그럼 건투를 비네!\n\n\n\n\n\n")
# time.sleep(3)
# # 튜토리얼 끝
# # 게임 인트로 끝

if user_occupation == "전사":
    user = Player(user_name, 200, 14, user_occupation, True, 0, 100)
elif user_occupation == "궁수":
    user = Player(user_name, 160, 18, user_occupation, True, 0, 100)
elif user_occupation == "주술사":
    user = Player(user_name, 120, 22, user_occupation, True, 0, 100)

stage = 1

print("")
monster_name = input(
    f"{Colors.BRIGHT_RED}몬스터 이름을 지정해 주세요{Colors.RESET} : ")
monster = Monster(monster_name, random.randrange(
    100, 150), random.randrange(12, 16), True)
print("")
print("="*80)
# time.sleep(1)

print("")
print(f"{Colors.BRIGHT_YELLOW}{user.name}{Colors.RESET}의 {Colors.RED}hp{Colors.RESET}는 {Colors.RED}{user.max_hp}{Colors.RESET} 입니다")
print(f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.BLUE}mp{Colors.RESET}는 {Colors.BLUE}{user.max_mp}{Colors.RESET} 입니다")
print(f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.MAGENTA}power{Colors.RESET}는 {Colors.MAGENTA}{user.power}{Colors.RESET} 입니다")
print("")
print(f"{Colors.BRIGHT_RED}{monster.name}{Colors.RESET}의 {Colors.RED}hp{Colors.RESET}는 {Colors.RED}{monster.max_hp}{Colors.RESET} 입니다")
print(f"{Colors.BRIGHT_RED}{monster.name}{Colors.RESET}의 {Colors.MAGENTA}power{Colors.RESET}는 {Colors.MAGENTA}{monster.power}{Colors.RESET} 입니다")
print("")
print("="*80)

while (True):
    user.skill()
    if monster.alive == True:
        if user.defense_success == True:
            print(
                f"{Colors.YELLOW}{user.name}{Colors.RESET}의 방어 성공! 추가로 hp와 mp가 회복됩니다")
            monster.show_status()
        else:
            user.attack(monster)
            monster.show_status()
    if user.alive == True:
        if user.defense_success == True:
            print(
                f"{Colors.BRIGHT_RED}{monster.name}{Colors.RESET}의 공격이 막혔습니다!")
            user.show_status()
            user.defense_success = False
        else:
            monster.attack(user)
            user.show_status()
    print("="*80)
    if user.alive == False:
        print(f'{Colors.RED}You Died ...{Colors.RESET}')
        print(
            f"현재 {Colors.BRIGHT_YELLOW}{user.gold}gold{Colors.RESET}를 가지고 있습니다")
        print("="*80+"\n")

        end = input("부활 하시겠습니까? (Y/N or Press any key) : ")
        if end == "Y" or end == "y":
            user.hp = user.max_hp
            user.mp = user.max_mp
            user.alive = True
            print("\n"+"="*80)
            continue
    elif monster.alive == False:
        print(f'{Colors.YELLOW}축하합니다 몬스터를 쓰려트렸습니다 !{Colors.RESET}')
        print(
            f"현재 {Colors.BRIGHT_YELLOW}{user.gold}gold{Colors.RESET}를 가지고 있습니다")
        print(
            f"현재 {Colors.BRIGHT_YELLOW}{user.exp}exp{Colors.RESET}를 가지고 있습니다\n")

        print(
            f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.RED}남은 hp는 {user.hp}{Colors.RESET} 입니다")
        print(
            f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.BLUE}남은 mp는 {user.mp}{Colors.RESET} 입니다")
        print("="*80)
        time.sleep(2)
        os.system("clear")
        break


while True:
    user.fight = False
    print("="*80+"\n")
    print(f"{Colors.RED}hp : {user.hp}/{user.max_hp}{Colors.RESET}")
    print(f"{Colors.BLUE}mp : {user.mp}/{user.max_mp}{Colors.RESET}")
    print(f"{Colors.MAGENTA}power : {user.power}{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}gold : {user.gold}{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}exp : {user.exp}{Colors.RESET}")
    print("\n"+"="*80)
    town = input(f"\n아저씨의 오두막입니다. 무엇을 이용하시겠습니까? ({Colors.RED}1. 마왕의 탑( %d층 ){Colors.RESET} {Colors.BLUE}2. 상점{Colors.RESET}  {Colors.GREEN}3. 가방{Colors.RESET}) : " %stage)
    os.system("clear")
    # time.sleep(1)
    
    if town == '1':
        user.fight = True
        print("="*80)
        print(f'\n{Colors.RED}stage : {stage}{Colors.RESET}\n')
        print("="*80)
        stage += 1

        if stage <= 5:
            monster = Monster("고블린", random.randrange(250, 300), random.randrange(12, 16), True)
        elif stage < 10:
            monster = Monster("오크", random.randrange(300, 350), random.randrange(16, 20), True)
        else:
            monster = Monster("오두막 아저씨(흑막)", random.randrange(500), random.randrange(30), True)

        while (True):
            user.skill()
            if monster.alive == True:
                if user.defense_success == True:
                    print(
                        f"{Colors.YELLOW}{user.name}{Colors.RESET}의 방어 성공! 추가로 hp와 mp가 회복됩니다")
                    monster.show_status()
                else:
                    user.attack(monster)
                    monster.show_status()
            if user.alive == True:
                if user.defense_success == True:
                    print(
                        f"{Colors.BRIGHT_RED}{monster.name}{Colors.RESET}의 공격이 막혔습니다!")
                    user.show_status()
                    user.defense_success = False
                else:
                    monster.attack(user)
                    user.show_status()
            print("="*80)

            if user.alive == False:
                print(f'{Colors.RED}You Died ...{Colors.RESET}')
                print(
                    f"현재 {Colors.BRIGHT_YELLOW}{user.gold}gold{Colors.RESET}를 가지고 있습니다")
                print("="*80+"\n")

                end = input("부활 하시겠습니까? (Y/N or Press any key) : ")
                if end == "Y" or end == "y":
                    user.hp = user.max_hp
                    user.mp = user.max_mp
                    user.alive = True
                    print("\n"+"="*80)
                    continue
            elif monster.alive == False:
                print(f'{Colors.YELLOW}축하합니다 몬스터를 쓰려트렸습니다 !{Colors.RESET}')
                print(
                    f"현재 {Colors.BRIGHT_YELLOW}{user.gold}gold{Colors.RESET}를 가지고 있습니다")
                print(
                    f"현재 {Colors.BRIGHT_YELLOW}{user.exp}exp{Colors.RESET}를 가지고 있습니다\n")

                print(
                    f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.RED}남은 hp는 {user.hp}{Colors.RESET} 입니다")
                print(
                    f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.BLUE}남은 mp는 {user.mp}{Colors.RESET} 입니다")
                print("="*80)
                print(f'\n\n{stage}층으로 넘어갑니다.....\n\n')
                break

        if stage == 10:
            subprocess.call(["python", "ending.py"])
            break

        # monster.alive = True
        # monster.hp = monster.max_hp
    # 상점 이용하기      
    elif town == '2':
        user.fight = False
        store = Store()
        print("\n상점에 오신걸 환영합니다! \n")
        select_ = input("어떤 상점을 이용하시겠습니까? (1. 무기상점  2. 방어구상점  3.포션상점  4.나가기) : ")
        os.system("clear")

        # 무기
        if select_ == '1':
            if user_occupation == "전사":
                print("="*35 + "  Menu  " + "="*35 + "\n")
                num = 0
                for n in store.weapon_warrior:
                    num = num + 1
                    print("%d. " % num + store.weapon_warrior[n])

                print("\n" + "="*78 + "\n")
                buy = input("어떤 물건을 구매 하시겠습니까? (1 ~ 5) : ")
                print(store.weapon_warrior[buy]+" 을(를) 구매 했습니다. \n")
                # 구매한 아이템을 장작할지 물어보고 장착하면 능력치가 올라가게 만들어야함

                put_on = input("구매한 무기를 장착하시겠습니까? (Y/N) : ")
                if put_on == 'y' or put_on == 'Y':
                    store.buy_weapon(store.weapon_warrior[buy], user)
                    print(f"\n{user.name}의 power는 {user.power}입니다.\n")
                    print("="*80)    
            elif user_occupation == "궁수":
                print("="*35 + "  Menu  " + "="*35 + "\n")
                num = 0
                for n in store.weapon_warrior:
                    num = num + 1
                    print("%d. " % num + store.weapon_archer[n])

                print("\n" + "="*78 + "\n")
                buy = input("어떤 물건을 구매 하시겠습니까? (1 ~ 5) : ")
                print(store.weapon_archer[buy]+" 을(를) 구매 했습니다. \n")
                # 구매한 아이템을 장작할지 물어보고 장착하면 능력치가 올라가게 만들어야함
                
                put_on = input("구매한 무기를 장착하시겠습니까? (Y/N) : ")
                if put_on == 'y' or put_on == 'Y':
                    store.buy_weapon(store.weapon_archer[buy], user)
                    print(f"\n{user.name}의 power는 {user.power}입니다.\n")
                    print("="*80)    
            elif user_occupation == "주술사":
                print("="*35 + "  Menu  " + "="*35 + "\n")
                num = 0
                for n in store.weapon_warrior:
                    num = num + 1
                    print("%d. " % num + store.weapon_wizard[n]) 

                print("\n" + "="*78 + "\n")
                buy = input("어떤 물건을 구매 하시겠습니까? (1 ~ 5) : ")
                print(store.weapon_wizard[buy]+" 을(를) 구매 했습니다. \n")
                # 구매한 아이템을 장작할지 물어보고 장착하면 능력치가 올라가게 만들어야함
                
                put_on = input("구매한 무기를 장착하시겠습니까? (Y/N) : ")
                if put_on == 'y' or put_on == 'Y':
                    store.buy_weapon(store.weapon_warrior[buy], user)
                    print(f"\n{user.name}의 power는 {user.power}입니다.\n")
                    print("="*80) 
            # elif put_on == 'n' or put_on == 'N':
                # 가방으로 넣기

            # 구매한 아이템의 정보를 가방에 넣어줘야함 > 가방 클래스를 만들어서
            # buy_list += store.weapon_warrior[buy]
            # result = ''.join(buy_list) or result = ''.join(str(s) for s in buy_list)
            # print(''.join(buy_list))
            # for s in buy_list:
            #     print(s, end="")
            time.sleep(2)
            os.system("clear")
        # 방어구
        elif select_ == '2':
            print("="*35 + "  Menu  " + "="*35 + "\n")
            num = 0
            for n in store.armor_all:
                num = num + 1
                print("%d. " % num + store.armor_all[n])

            print("\n" + "="*78 + "\n")
            buy = input("어떤 물건을 구매 하시겠습니까? (1 ~ 5) : ")
            print(store.armor_all[buy]+" 을(를) 구매 했습니다. \n")
            # 구매한 아이템을 장작할지 물어보고 장착하면 능력치가 올라가게 만들어야함

            put_on = input("구매한 방어구를 장착하시겠습니까? (Y/N) : ")
            if put_on == 'y' or put_on == 'Y':
                store.buy_armor(store.armor_all[buy], user)
                print(f"\n{user.name}의 hp는 {user.hp}/{user.max_hp}입니다.")
                print(f"{user.name}의 mp는 {user.mp}/{user.max_mp}입니다.\n")
                print("="*80)
            time.sleep(2)
            os.system("clear")
        # 포션
        elif select_ == '3':
            print("="*35 + "  Menu  " + "="*35 + "\n")
            num = 0
            for n in store.potion:
                num = num + 1
                print("%d. " % num + store.potion[n])

            print("\n" + "="*78 + "\n")
            buy = input("어떤 물건을 구매 하시겠습니까? (1 ~ 2) : ")
            print(store.potion[buy]+" 을(를) 구매 했습니다. \n")
            store.buy_potion(store.potion[buy], user)
            time.sleep(2)
            os.system("clear")
        # 상점 나가기        
        elif select_ == '4':
            continue

    # 가방(인벤토리) 확인하기
    elif town == '3':
        user.inventory()
    else:
        print("장난치지마!")
