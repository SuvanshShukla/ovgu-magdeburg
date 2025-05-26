public class ConsoleVisualizer implements IMonsterVisualizer{

    @Override
    public void visualize(Monster monster) {
        System.out.println(monster.getName());
    }
}
