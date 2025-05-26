public interface IMonster {

    String getName();

    int getHealth();

    int getMaxHealth();

    boolean isAlive();

    void receiveDamage(int damage);

    int getBaseAttack();

    int getAttack();

    float getWeight();

    void setAttackMultiplier(float multiplier);

}
