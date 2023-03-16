/**
 * 上文已经讨论过，所有的 JavaScript 对象都从 Object.prototype 继承属性（除了那些不通过原型显式创建的对象）。
 * 这些继承属性主要是方法，因为 JavaScript 程序员普遍对继承方法更感兴趣。
 * 例如我们已经见过的 hasOwnProperty() 和 propertyIsEnumerable() 方法。
 * （并且我们也已经提到了一小部分定义在对象构造函数中的静态函数，像 Object.create() 和 Object.keys()。）
 * 本节介绍在 Object.prototype 上定义的少数通用对象方法，但是这些方法经常会被更专业的实现所取代。
 * 在下面的各节中，我们将展示在单个对象上定义这些方法的示例。在第 9 章中，将学习如何更常规化地为整个对象类定义这些方法。
 */

