# The `@Override` annotation should be used as often as possible

A good [stack-overflow answer on why](https://stackoverflow.com/a/212624)

Here's what is says:

You should use @Override whenever possible. It prevents simple mistakes from being made. Example:

```java
class C {
    @Override
    public boolean equals(SomeClass obj){
        // code ...
    }
}
```

This doesn't compile because it doesn't properly override public boolean equals(Object obj).

The same will go for methods that implement an interface (1.6 and above only) or override a Super class's method.

Note here that the second `equals()` method he writes takes a generic `Object` class object. But the method we wrote takes a custom `SomeClass` object.

