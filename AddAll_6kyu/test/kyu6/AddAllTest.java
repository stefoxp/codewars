package kyu6;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author stefano
 */
public class AddAllTest {
    
    public AddAllTest() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }

    /**
     * Test of addAll method, of class AddAll.
     */
    @Test
    public void testAddAllBasic() {
        System.out.println("addAllBasic");
        /*
        int[] numbers = null;
        int expResult = 0;
        int result = AddAll.addAll(numbers);
        assertEquals(expResult, result);
        */
        // int[] numbers = {1,2,3};
        assertEquals(9, AddAll.addAll(new int[] {1,2,3}));
        // TODO review the generated test code and remove the default call to fail.
        // fail("The test case is a prototype.");
    }
    
}
