import java.util.ArrayList;
import java.util.Iterator;

public class Set<T> {

    private ArrayList<T> items;

    public Set() {
        items = new ArrayList<>();
    }

    public int size() {
        return items.size();
    }

    public boolean addItem(T t) {
        if (!items.contains(t)){
            items.add(t);
            return true;
        } else {
            return false;
        }
    }

    public boolean removeItem(T t) {
        return items.remove(t);
    }

    public boolean contains(T t) {
        return items.contains(t);
    }
 }
