import org.junit.Test;

import static org.junit.Assert.*;

public class SetTest {

    /* ********************************************************************************************************* */
    /*                                        Your work starts here!                                             */
    /* ********************************************************************************************************* */

    @Test
    public void test_addItem() {
        Set<Integer> s = new Set<>();
        assertTrue("The value should be true!", s.addItem(1));
        assertFalse("The value should be false!", s.addItem(1));
        assertEquals("Size of the set should still be 1", 1, s.size());
        assertNotEquals("The set should not contain 2", true, s.contains(2));
    }

    @Test
    public void test_removeItem() {
        Set<Integer> s = new Set<>();
        s.addItem(1);
        s.removeItem(1);
        assertTrue("We should be able to remove the new item", s.size() == 0);
        assertFalse("1 Should no longer be in the set", s.contains(1));
        assertEquals("Size should be 0.", 0, s.size());
        assertNotEquals("There should be no  other item present in the set anymore", true, s.contains(2));
    }

    @Test
    public void contains() {
        Set<Integer> s = new Set<>();
        s.addItem(1);
        assertTrue("The set should contain 1.", s.contains(1));
        assertFalse("The set shouldn't contain 5.", s.contains(5));
        assertEquals("The size of the set should be 1", 1, s.size());
        assertNotEquals("The set shouldn't have another 1.", true, s.addItem(1));
    }

    @Test
    public void size() {
        Set<Integer> s = new Set<>();
        s.addItem(1);
        assertTrue("We should be able to add 2 to the set.", s.addItem(2));
        assertFalse("We should not be able to add 1 to the set again.", s.addItem(1));
        assertEquals("The set should only have two values.", 2, s.size());
        assertNotEquals("The set should not contain 3 as a value.", true, s.contains(3));
    }
}