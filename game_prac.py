import random
from Color import Colors


class Character():
    mp = 100
    max_mp = 100
    new_power = 0
    critical = 0
    defense = 0
    experience = 0
    alive = True
    recovery_item = 2
    recovery_item_max = 5
    gold = 100
    defense_success = False

    def __init__(self, name, hp, power, occupation):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.occupation = occupation

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
                self.new_power = 0
                if self.recovery_item > 0:
                    if self.hp < self.max_hp:
                        self.recovery_item = self.recovery_item - 1
                        self.hp = max(self.hp + 50, 0)
                        print(f"{Colors.RED}HP recovers by 50 !{Colors.RESET}")
                        if self.hp > self.max_hp:
                            self.hp = self.max_hp
                    else:
                        print(f"{Colors.RED}체력이 가득 차있습니다{Colors.RESET}")
                        print("="*80)
                        return self.skill()
                else:
                    print(f"{Colors.YELLOW}hp물약을 가지고 있지 않습니다{Colors.RESET}")
                    print("="*80)
                    return self.skill()
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
                self.new_power = 0
                if self.recovery_item > 0:
                    if self.hp < self.max_hp:
                        self.recovery_item = self.recovery_item - 1
                        self.hp = max(self.hp + 50, 0)
                        print(f"{Colors.RED}HP recovers by 50 !{Colors.RESET}")
                        if self.hp > self.max_hp:
                            self.hp = self.max_h
                    else:
                        print(f"{Colors.RED}체력이 가득 차있습니다{Colors.RESET}")
                        print("="*80)
                        return self.skill()
                else:
                    print(f"{Colors.YELLOW}hp물약을 가지고 있지 않습니다{Colors.RESET}")
                    print("="*80)
                    return self.skill()
            else:
                print("다시 선택해 주세요")
                print("="*80)
                return self.skill()

        elif self.occupation == "마법사":
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
                self.new_power = 0
                if self.recovery_item > 0:
                    if self.hp < self.max_hp:
                        self.recovery_item = self.recovery_item - 1
                        self.hp = max(self.hp + 50, 0)
                        print(f"{Colors.RED}HP recovers by 50 !{Colors.RESET}")
                        if self.hp > self.max_hp:
                            self.hp = self.max_hp
                    else:
                        print(f"{Colors.RED}체력이 가득 차있습니다{Colors.RESET}")
                        print("="*80)
                        return self.skill()
                else:
                    print(f"{Colors.YELLOW}hp물약을 가지고 있지 않습니다{Colors.RESET}")
                    print("="*80)
                    return self.skill()
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
            print(
                f'{Colors.RED}{other.name}{Colors.RESET}이(가) 쓰러졌습니다  {Colors.BRIGHT_YELLOW}{gold_m}gold{Colors.RESET}를 획득했습니다!')
            self.gold = self.gold + gold_m
            self.alive = False

    def show_status(self):
        print(
            f'{Colors.YELLOW}{self.name}{Colors.RESET}의 상태: {Colors.RED}HP {self.hp}{Colors.RESET}/{self.max_hp}  {Colors.BLUE}MP {self.mp}{Colors.RESET}/{self.max_mp}')


class Monster():
    power = random.randrange(12, 16)
    hp = random.randrange(250, 300)
    max_hp = hp
    alive = True

    def __init__(self, name):
        self.name = name

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
            self.alive = False

    def show_status(self):
        print(f'{Colors.BRIGHT_RED}{self.name}{Colors.RESET}의 상태: {Colors.RED}HP {self.hp}{Colors.RESET}/{self.max_hp}')


while (True):
    print("="*80)
    print("\n" + Colors.YELLOW+"welcome to" +
          Colors.GREEN+" 미니게임 !!! \n" + Colors.RESET)
    print("="*80)
    character = input(f"{Colors.YELLOW}캐릭터를 생성해 주세요{Colors.RESET} : ")
    while (True):
        occupation = input(
            f"{Colors.CYAN}직업 선택 (전사  궁수  마법사){Colors.RESET} : ")
        if occupation == "궁수" or occupation == "전사" or occupation == "마법사":
            break
        else:
            print("선택하진 직업은 존재하지 않습니다. 다시 선택해 주세요 \n")

    if occupation == "전사":
        user = Character(character, 200, 14, occupation)
    elif occupation == "궁수":
        user = Character(character, 160, 18, occupation)
    elif occupation == "마법사":
        user = Character(character, 120, 22, occupation)

    print("")
    monster_name = input(
        f"{Colors.BRIGHT_RED}몬스터 이름을 지정해 주세요{Colors.RESET} : ")
    monster = Monster(monster_name)
    print("="*80)

    print(f"{Colors.BRIGHT_YELLOW}{user.name}{Colors.RESET}의 {Colors.RED}hp{Colors.RESET}는 {Colors.RED}{user.max_hp}{Colors.RESET} 입니다")
    print(f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.BLUE}mp{Colors.RESET}는 {Colors.BLUE}{user.max_mp}{Colors.RESET} 입니다")
    print(f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.MAGENTA}power{Colors.RESET}는 {Colors.MAGENTA}{user.power}{Colors.RESET} 입니다")
    print("")
    print(f"{Colors.BRIGHT_RED}{monster.name}{Colors.RESET}의 {Colors.RED}hp{Colors.RESET}는 {Colors.RED}{monster.max_hp}{Colors.RESET} 입니다")
    print(f"{Colors.BRIGHT_RED}{monster.name}{Colors.RESET}의 {Colors.MAGENTA}power{Colors.RESET}는 {Colors.MAGENTA}{monster.power}{Colors.RESET} 입니다")
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
                print(f"{Colors.BRIGHT_RED}{monster.name}{Colors.RESET}의 공격이 막혔습니다!")
                user.show_status()
                user.defense_success = False
            else:
                monster.attack(user)
                user.show_status()
        print("="*80)
        if monster.alive == False:
            print(f'{Colors.RED}You Died ...{Colors.RESET}')
            print(
                f"현재 {Colors.BRIGHT_YELLOW}{user.gold}gold{Colors.RESET}를 가지고 있습니다")
            print("="*80)
            break
        elif user.alive == False:
            print(f'{Colors.YELLOW}축하합니다 당신은 몬스터를 쓰려트렸습니다 !{Colors.RESET}')
            print(
                f"현재 {Colors.BRIGHT_YELLOW}{user.gold}gold{Colors.RESET}를 가지고 있습니다 \n")
            print(
                f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.RED}남은 hp는 {user.hp}{Colors.RESET} 입니다")
            print(
                f"{Colors.YELLOW}{user.name}{Colors.RESET}의 {Colors.BLUE}남은 mp는 {user.mp}{Colors.RESET} 입니다")
            print("="*80)
            break

    end = input("재시작 하시겠습니까? (Y/N or Press any key) : ")
    print("="*80)
    if end == "Y" or end == "y":
        continue
    else:
        break
