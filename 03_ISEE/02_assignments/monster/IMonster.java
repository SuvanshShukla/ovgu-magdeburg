public interface IMonster {
    /** Return the name of the Monster */
    public String getName();

    /** Return the current health points; returnd value is positive or 0. */
    public float getHealth();

    /** Access the maximum value for health points. Value must be bigger than 0. */
    public float getMaxHealth();

    /** Return true if the number of health points is bigger than 0. */
    public boolean isAlive();

    /** Access the base attack. */
    public float getBaseAttack();

    /** Access the attack value. */
    public int getAttack();

    /** Access the weight in kg. */
    public float getWeight();

    /** Set the scale factor for the attack value. */
    public void setAttackMultiplier(float multiplier);

    void receiveDamage(float damage);

    void augmentAttack(float mult);

}
