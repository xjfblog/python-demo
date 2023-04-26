# https://github.com/robotze/GithubDesktopZhTool.git
import random
import time

# 角色属性
name = input('请输入您的角色名:')
hp = 100  # 生命值
atk = 50  # 攻击力
defense = 10  # 防御力

# 怪物属性
monsters = ['狼人', '刺猬', '巨人']
wolf_hp = 80
wolf_atk = 30
hedgehog_hp = 60
hedgehog_atk = 35
giant_hp = 120
giant_atk = 45

# 物品属性
items = ['药水', '镜子', '木棍']
potion_heal = 30
mirror_escape = True
stick_atk = 15

# 探险
print(f'冒险开始!{name}拥有{hp}生命值和{atk}攻击力。')
time.sleep(1)
print('在森林中有三种怪物:狼人、刺猬和巨人。你必须打败它们才能继续前进!')
time.sleep(2)

while hp > 0:
    # 遇敌
    enemy = random.choice(monsters)
    if enemy == '狼人':
        enemy_hp = wolf_hp
        enemy_atk = wolf_atk
    elif enemy == '刺猬':
        enemy_hp = hedgehog_hp
        enemy_atk = hedgehog_atk
    else:
        enemy_hp = giant_hp
        enemy_atk = giant_atk

    print(f'遇到了{enemy},它有{enemy_hp}生命值和{enemy_atk}攻击力!')

    # 战斗
    while enemy_hp > 0 and hp > 0:
        # 选择行动
        action = input('请选择行动:攻击(a)或使用物品(b):')
        if action == 'a':
            # 攻击
            enemy_hp -= atk
            hp -= enemy_atk
            print(f'{enemy}受到{atk}点伤害。{name}受到{enemy_atk}点伤害。')
            print(f'{name}剩余{hp}生命值。{enemy}剩余{enemy_hp}生命值。')
        elif action == 'b':
            # 使用物品
            item = random.choice(items)
            if item == '药水':
                hp += potion_heal
                print(f'{name}使用了药水,生命值恢复了{potion_heal}点!')
            elif item == '镜子':
                print(f'{name}使用了镜子,成功逃脱了战斗!')
                break
            else:
                atk += stick_atk
                print(f'{name}使用了木棍,攻击力增加到{atk}!')

    # 战斗结果
    if hp > 0 and enemy_hp <= 0:
        print(f'{name}成功打败了{enemy}!')
    elif hp <= 0:
        print('您失败了!GAME OVER!')
        break
    else:
        print('您逃脱了这场战斗!')

# 游戏结束
if hp > 0:
    print(f'{name}完成了所有战斗,获得了胜利!')
print('游戏结束,感谢您的参与!')
