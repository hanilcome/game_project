import random
from Color import Colors
import os
import time

# 민영_class Character를 만들고 player와 monster이 상속받을 수 있게 나눔


class Character():
    alive = True
    lavel = 1

    def __init__(self, name, hp, power, lavel, alive):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.lavel = lavel
        self.alive = alive

    def show_status(self):
        print(f'{Colors.YELLOW}{self.name}{Colors.RESET}의 상태: {Colors.RED}HP {self.hp}{Colors.RESET}/{self.max_hp}  {Colors.BLUE}MP {self.mp}{Colors.RESET}/{self.max_mp}')


class Player(Character):
    mp = 100
    max_mp = mp
    new_power = 0
    critical = 0
    defense = 0
    experience = 0
    gold = 100
    defense_success = False
    hp_potion = 3
    mp_potion = 3
    fight = False

    # lavel, exp, max_exp추가함

    def __init__(self, name, hp, power, occupation, alive, lavel, exp, max_exp):
        self.exp = exp
        self.max_exp = max_exp
        self.occupation = occupation  # ??
        super().__init__(name, hp, power, lavel, alive)

    def skill(self):
        if self.occupation == "전사":
            set = input(f"{Colors.GREEN}스킬 선택 ({Colors.RESET}1.Normal Attack  {Colors.RED}2.Magic Attack{Colors.RESET}  {Colors.BLUE}3.Defense{Colors.RESET}  {Colors.GREEN}4.HP Recovery){Colors.RESET} : ")
            # 1. Normal Attack
            if set == '1':
                self.critical = random.randrange(1, 100)
                if self.critical <= 20:
                    print(Colors.RED + "Critical !"+Colors.RESET)
                    self.new_power = random.randrange(
                        self.power + 10, self.power + 18)
                else:
                    self.new_power = random.randrange(
                        self.power - 2, self.power + 2)
            # 2. Magic Attack
            elif set == '2':
                if self.mp > 0:
                    self.mp = max(self.mp - 25, 0)
                    self.critical = random.randrange(1, 100)
                    if self.critical <= 10:
                        print(Colors.RED + "Critical !"+Colors.RESET)
                        self.new_power = random.randrange(
                            self.power + 14, self.power + 42)
                    else:
                        self.new_power = random.randrange(
                            self.power, self.power + 14)
                else:

                    print(f"{Colors.BLUE}MP가 부족합니다{Colors.RESET}")
                    print("="*80)
                    return self.skill()
            # 3. Defense
            elif set == '3':
                self.new_power = 0
                self.defense = random.randrange(1, 100)
                if self.defense <= 30:
                    self.defense_success = True
                    if self.hp < self.max_hp:
                        self.hp = max(self.hp + 25, 0)
                        if self.hp > self.max_hp:
                            self.hp = self.max_hp
                    if self.mp < self.max_mp:
                        self.mp = max(self.mp + 25, 0)
                    print(
                        f"{Colors.YELLOW}Successful defense!{Colors.RESET} {Colors.RED}HP recovers by 25{Colors.RESET} {Colors.BLUE}MP recovers by 25{Colors.RESET}")
                else:
                    self.defense_success = False
                    print(f"{Colors.RED}Failed to defend!{Colors.RESET}")
            # 4. HP Recovery
            elif set == '4':
                self.inventory()
                # self.new_power = 0
                # if self.hp_potion > 0:
                #     if self.hp < self.max_hp:
                #         self.hp_potion = self.hp_potion - 1
                #         self.hp = max(self.hp + 50, 0)
                #         print(f"{Colors.RED}HP recovers by 50 !{Colors.RESET}")
                #         if self.hp > self.max_hp:
                #             self.hp = self.max_hp
                #     else:
                #         print(f"{Colors.RED}체력이 가득 차있습니다{Colors.RESET}")
                #         print("="*80)
                #         return self.skill()
                # else:
                #     print(f"{Colors.YELLOW}hp물약을 가지고 있지 않습니다{Colors.RESET}")
                #     print("="*80)
                #     return self.skill()
            else:
                print("다시 선택해 주세요")
                print("="*80)
                return self.skill()

        elif self.occupation == "궁수":
            set = input(f"{Colors.GREEN}스킬 선택 ({Colors.RESET}1.Normal Attack  {Colors.RED}2.Magic Attack{Colors.RESET}  {Colors.BLUE}3.Defense{Colors.RESET}  {Colors.GREEN}4.HP Recovery){Colors.RESET} : ")
            # 1. Normal Attack
            if set == '1':
                self.critical = random.randrange(1, 100)
                if self.critical <= 20:
                    print(Colors.RED + "Critical !"+Colors.RESET)
                    self.new_power = random.randrange(
                        self.power + 14, self.power + 22)
                else:
                    self.new_power = random.randrange(
                        self.power - 2, self.power + 2)
            # 2. Magic Attack
            elif set == '2':
                if self.mp > 0:
                    self.mp = max(self.mp - 25, 0)
                    self.critical = random.randrange(1, 100)
                    if self.critical <= 10:
                        print(Colors.RED + "Critical !"+Colors.RESET)
                        self.new_power = random.randrange(
                            self.power + 18, self.power + 54)
                    else:
                        self.new_power = random.randrange(
                            self.power, self.power + 18)
                else:
                    print(f"{Colors.BLUE}MP가 부족합니다{Colors.RESET}")
                    print("="*80)
                    return self.skill()
            # 3. Defense
            elif set == '3':
                self.new_power = 0
                self.defense = random.randrange(1, 100)
                if self.defense <= 30:
                    self.defense_success = True
                    if self.hp < self.max_hp:
                        self.hp = max(self.hp + 25, 0)
                        if self.hp > self.max_hp:
                            self.hp = self.max_hp
                    if self.mp < self.max_mp:
                        self.mp = max(self.mp + 25, 0)
                    print(
                        f"{Colors.YELLOW}Successful defense!{Colors.RESET} {Colors.RED}HP recovers by 25{Colors.RESET} {Colors.BLUE}MP recovers by 25{Colors.RESET}")
                else:
                    self.defense_success = False
                    print(f"{Colors.RED}Failed to defend!{Colors.RESET}")
            # 4. HP Recovery
            elif set == '4':
                self.inventory()
            else:
                print("다시 선택해 주세요")
                print("="*80)
                return self.skill()

        elif self.occupation == "주술사":
            set = input(f"{Colors.GREEN}스킬 선택 ({Colors.RESET}1.Normal Attack  {Colors.RED}2.Magic Attack{Colors.RESET}  {Colors.BLUE}3.Defense{Colors.RESET}  {Colors.GREEN}4.HP Recovery){Colors.RESET} : ")
            # 1. Normal Attack
            if set == '1':
                self.critical = random.randrange(1, 100)
                if self.critical <= 10:
                    print(Colors.RED + "Critical !"+Colors.RESET)
                    self.new_power = random.randrange(
                        self.power + 18, self.power + 26)
                else:
                    self.new_power = random.randrange(
                        self.power - 2, self.power + 2)
            # 2. Magic Attack
            elif set == '2':
                if self.mp > 0:
                    self.mp = max(self.mp - 25, 0)
                    self.critical = random.randrange(1, 100)
                    if self.critical <= 20:
                        print(Colors.RED + "Critical !"+Colors.RESET)
                        self.new_power = random.randrange(
                            self.power + 22, self.power + 66)
                    else:
                        self.new_power = random.randrange(
                            self.power, self.power + 22)
                else:
                    print(f"{Colors.BLUE}MP가 부족합니다{Colors.RESET}")
                    print("="*80)
                    return self.skill()
            # 3. Defense
            elif set == '3':
                self.new_power = 0
                self.defense = random.randrange(1, 100)
                if self.defense <= 30:
                    self.defense_success = True
                    if self.hp < self.max_hp:
                        self.hp = max(self.hp + 25, 0)
                        if self.hp > self.max_hp:
                            self.hp = self.max_h
                    if self.mp < self.max_mp:
                        self.mp = max(self.mp + 25, 0)
                    print(
                        f"{Colors.YELLOW}Successful defense!{Colors.RESET} {Colors.RED}HP recovers by 25{Colors.RESET} {Colors.BLUE}MP recovers by 25{Colors.RESET}")
                else:
                    self.defense_success = False
                    print(f"{Colors.RED}Failed to defend!{Colors.RESET}")
            # 4. HP Recovery
            elif set == '4':
                self.inventory()
            else:
                print("다시 선택해 주세요")
                print("="*80)
                return self.skill()

    def attack(self, other):
        damage = self.new_power
        other.hp = max(other.hp - damage, 0)
        print(f'{Colors.YELLOW}{self.name}{Colors.RESET}의 공격! {Colors.BRIGHT_RED}{other.name}{Colors.RESET}에게 {Colors.RED}{damage}의 데미지{Colors.RESET}를 입혔습니다')
        if other.hp <= 0:
            gold_m = random.randrange(50, 100)
            death_exp = 50
            print(
                f'{Colors.RED}{other.name}{Colors.RESET}이(가) 쓰러졌습니다  {Colors.BRIGHT_YELLOW}{gold_m}gold{Colors.RESET}를 획득했습니다!')
            self.gold = self.gold + gold_m
            self.exp = self.exp + death_exp
            other.alive = False

    def inventory(self):
        while True:
            print(
                f"1. hp potion : {self.hp_potion}\t2. mp potion : {self.mp_potion}\t3. 뒤로 가기")
            choose_item_use = input("어떤 아이템을 사용하겠습니까?\t")
            if choose_item_use == '1':
                if self.hp_potion > 0:
                    print('hp potion을 사용합니다.')
                    self.hp_potion -= 1
                    self.hp = self.hp + 50
                    if self.hp > self.max_hp:
                        self.hp = self.max_hp
                    print(f'{self.name}의 체력은 {self.hp}/{self.max_hp}입니다.')
                    break
                else:
                    print('hp potion이 부족합니다. 사용할수 없습니다.')
                    continue
            elif choose_item_use == '2':
                if self.mp_potion > 0:
                    print('mp potion을 사용합니다.')
                    self.mp_potion -= 1
                    self.mp = self.mp + 20
                    if self.mp > self.max_mp:
                        self.mp = self.max_mp
                    print(f'{self.name}의 마나는 {self.mp}/{self.max_mp}입니다.')
                    break
                else:
                    print('mp potion이 부족합니다. 사용할수 없습니다.')
                    continue
            elif choose_item_use == '3':
                if self.fight == True:
                    return self.skill()
                else:
                    break

    # 민영_경험치 획득시 호출하는 함수
    # def gain_exp(monster_death_exp):
    #     Player.exp += monster_death_exp
    #     if Player.exp >= Player.max_exp:
    #         Player.lavel += 1
    #         Player.max_exp += 10

    # 민영_경험치 획득시 호출하여 경험치 증가
    def gain_exp(self, monster_death_exp):
        self.exp += monster_death_exp  # 몬스터가 죽으면 나오는 경험치
        self.level_up()  # 레벨업함수 호출

    def level_up(self):
        if self.exp >= self.max_exp:  # 맥스경험치 보다 현재 경험치가 많으면
            self.lavel += 1  # 레벨업
            self.max_exp += 10  # 맥스경험치 10 올리기
            self.hp = self.max_hp  # hp회복
            self.mp = self.max_mp  # mp회복
            self.power += 1+1*(self.lavel/2)  # power올리기
            self.exp = 0  # 경험치 초기화
            print("f{self.name} 레벨업! 축하합니다! 현재레벨: {self.lavel}")


class Monster(Character):
    def __init__(self, name, hp, power, alive, lavel):  # monster_death_exp 랜덤으로?
        super().__init__(name, hp, power, lavel, alive)

    def attack(self, other):
        self.critical = random.randrange(1, 100)
        if self.critical <= 10:
            print(Colors.RED + "Critical !"+Colors.RESET)
            damage = random.randrange(self.power + 12, self.power + 16)
        else:
            damage = random.randrange(self.power - 4, self.power + 4)
        other.hp = max(other.hp - damage, 0)
        print(f'{Colors.BRIGHT_RED}{self.name}{Colors.RESET}의 공격! {Colors.YELLOW}{other.name}{Colors.RESET}에게 {Colors.RED}{damage}의 데미지{Colors.RESET}를 입혔습니다')
        if other.hp <= 0:
            gold = random.randrange(50, 100)
            print(f'{Colors.YELLOW}{other.name}{Colors.RESET}이(가) 쓰러졌습니다  {Colors.BRIGHT_YELLOW}{gold}gold{Colors.RESET}를 잃었습니다.')
            other.gold = other.gold - gold
            other.alive = False
    
    def show_status(self):
        print(f'{Colors.YELLOW}{self.name}{Colors.RESET}의 상태: {Colors.RED}HP {self.hp}{Colors.RESET}/{self.max_hp}')