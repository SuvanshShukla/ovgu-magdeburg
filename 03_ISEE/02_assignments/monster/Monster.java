//Submission for Exercise 2 Task 4: Class Monster
//Author: Suvansh Shukla
//Matriculation Number: 256245
public class Monster implements IMonster{

    String name;
    int maxHp;
    int hp;
    float weight;
    float mult;
    int attack;

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public int getHealth() {
        return Math.max(this.hp, 0);
    }

    @Override
    public int getMaxHealth() {
        return Math.max(this.maxHp, 1);
    }

    /**
     * Checks if hp value is greater than 0
     * if greater than 0 then monster is still alive (true)
     * otherwise it is dead (false).
     * @return boolean
     */
    @Override
    public boolean isAlive() {
        return this.hp > 0;
    }

    @Override
    public int getBaseAttack() {
        return this.attack;
    }

    @Override
    public int getAttack() {
        return (int) (this.attack * this.mult);
    }

    @Override
    public float getWeight() {
        return this.weight;
    }

    /**
     * This method sets the multiplier with the condition its value
     * must be between -2.0 & 5.0
     * @param multiplier float
     */
    @Override
    public void setAttackMultiplier(float multiplier) {
        if (multiplier > 5.0f) {
            this.mult = 5.0f;
        } else if (multiplier < -2.0f) {
            this.mult = -2.0f;
        } else {
            this.mult = multiplier;
        }
    }

    /**
     * Reduce hp by damage taken.
     * Damage taken is reduced if weight of the monster is greater than 13.7kg
     * @param damage any float
     */
    @Override
    public void receiveDamage(int damage) {
        if (this.weight > 13.37) {
            damage = (int) (damage * 0.8f);
        }
        this.hp = this.hp - damage;
        if (this.hp < 0){
            this.hp = 0;
        } else if (this.hp > this.maxHp) {
           this.hp = maxHp;
        }
    }

    /**
     * Constructs an object of the monster class
     * @param name name of the monster
     * @param maxHp max health points of the monster, cannot be less than 1
     * @param weight weight of the monster in kg, must be at least 100g
     * @param attack attack value, must be an int
     * @param mult attack value multiplier, must be between -2.0 and 5.0
     */
    public Monster(String name, int maxHp, float weight, int attack, float mult) {

        if (weight <0.1) {
            this.weight = 0.1f;
        } else {
            this.weight = weight;
        }

        this.maxHp = Math.max(maxHp, 1);

        this.hp = maxHp;

        if (mult > 5.0f) {
            this.mult = 5.0f;
        } else if (mult < -2.0f) {
            this.mult = -2.0f;
        } else {
            this.mult = mult;
        }

        this.name = name;
        this.attack = attack;
    }
}

