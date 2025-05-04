//Submission for Exercise 2 Task 4: Class Monster
//Author: Suvansh Shukla
//Matriculation Number: 256245
public class Monster implements IMonster{

    String name;
    float maxHp;
    float hp;
    float weight;
    float mult;
    int attack;

    @Override
    public String getName() {
        return name;
    }

    @Override
    public float getHealth() {
        return hp;
    }

    @Override
    public float getMaxHealth() {
        return maxHp;
    }

    /**
     * Checks if hp value is greater than 0
     * if greater than 0 then monster is still alive (true)
     * otherwise it is dead (false).
     * @return boolean
     */
    @Override
    public boolean isAlive() {
        return hp > 0;
    }

    @Override
    public float getBaseAttack() {
        return attack;
    }

    @Override
    public int getAttack() {
        return attack;
    }

    @Override
    public float getWeight() {
        return weight;
    }

    /**
     * This method sets the multiplier with the condition its value
     * must be between -2.0 & 5.0
     * @param multiplier float
     */
    @Override
    public void setAttackMultiplier(float multiplier) {
        if (multiplier >= -2.0f && multiplier <= 5.0f) {
            mult = multiplier;
        }
    }

    /**
     * Reduce hp by damage taken.
     * Damage taken is reduced if weight of the monster is greater than 13.7kg
     * @param damage any float
     */
    @Override
    public void receiveDamage(float damage) {
        if (hp > 0.00) {
            if (weight > 13.37) {
                damage = (float) (damage - (0.2 * damage));
            }
            hp = hp - damage;
        }
    }

    /**
     * Strengthens or weakens the attack based on mult value
     * @param mult - float between -2.0 & 5.0
     */
    @Override
    public void augmentAttack(float mult){
        if (mult > -2.0f && mult <= 5.0) {
            attack = (int) (attack * mult);
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
    public Monster(String name, float maxHp, float weight, int attack, float mult) {

        if (weight <0.1) {
            this.weight = 0.1f;
        } else {
            this.weight = weight;
        }

        if (maxHp < 1) {
            this.maxHp = 1;
        } else {
            this.maxHp = maxHp;
        }

        if (mult >= -2.0f && mult <= 5.0f) {
            this.mult = mult;
        }

        this.name = name;
        this.attack = attack;
    }
}

