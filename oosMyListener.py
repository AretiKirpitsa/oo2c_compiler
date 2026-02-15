from oosListener import oosListener
from oosParser import oosParser

# ==========================================
#           SYMBOL TABLE CLASSES
# ==========================================

class class_method:
    def __init__(self, name, is_constructor=False):
        self.version = 1
        self.name = name
        self.is_constructor = is_constructor
        self.fields = {} 
        self.params = {}
        self.param_number = 0
        self.return_type = None

    def set_version(self, next):
        self.version = next
    
    def get_version(self):
        return self.version

    def set_return_type(self, return_type):
        self.return_type = return_type
    
    def get_return_type(self):
        return self.return_type

    def set_as_constructor(self):
        self.is_constructor = True

    def set_name(self, new_name):
        self.name = new_name

    def add_field(self, field_name, field_type, is_param=False):
        if field_name in self.fields:
            print(f"Field '{field_name}' is already declared in scope of '{self.name}' method")
            exit(0)
        if is_param:
            self.params[field_name] = field_type
            self.param_number += 1
        self.fields[field_name] = field_type

    def has_field(self, field_name, expected_type=None):
        if str(field_name) not in list(self.fields.keys()):
            return False
        if expected_type is not None:
            return str(self.fields.get(str(field_name))) == str(expected_type)
        return True
    
    def get_field_type(self, field_name):
        if (self.has_field(field_name)):
            return self.fields.get(field_name)

    def get_params(self):
        return self.params
    
    def get_method_with_version(self):
        return f"{self.name}_{self.version}"
    
    def get_name(self):
        return self.name
    
    def get_param_number(self):
        return self.param_number

    def __str__(self):
        params = ', '.join([f"{name}: {type_}" for name, type_ in self.fields.items()])
        return f"\n\tMethod name: {self.name}\n\tFields: [{params}]\n\tParameter num: {str(self.param_number)}\n\tVersion: {str(self.version)}\n\tReturns: {str(self.return_type)}\n\tConstructor: {str(self.is_constructor)}"


class class_info:
    def __init__(self, name):
        self.name = name
        self.inherits_from = [] 
        self.methods = {}
        self.constructor_number = 0
        self.fields = {}
    
    def add_inheritance(self, parent_class):    
        if isinstance(parent_class, class_info):
            self.inherits_from.append(parent_class)
        else:
            print("Error: add_inheritance adding something that is not instance.")
            exit(0)
    
    def add_method(self, method_name, is_constructor=False, return_type="void", global_method_versions={}):
        new_method = class_method(None)
        new_method.add_field("self_ptr", self.name, True)
        
        if is_constructor:
            self.constructor_number += 1
            new_method.set_return_type(self.name)
            new_method.set_name(method_name)
            new_method.is_constructor = True
        else:
            new_method.set_name(method_name)
            new_method.set_return_type(return_type)

        ver = global_method_versions.get(method_name)
        if ver == None:
            self.methods[method_name] = []
            self.methods[method_name].append(new_method)
            global_method_versions[method_name] = 1
        else:
            if self.methods.get(method_name) == None:
                self.methods[method_name] = []
            self.methods[method_name].append(new_method)
            new_method.set_version(ver+1)
            global_method_versions[method_name] = ver + 1

        return [method_name, new_method]
    
    def add_field_to_method(self, method_obj, field_name, field_type, is_param=False):
        if field_name in method_obj.fields:
            print(f"Field '{field_name}' is already declared in scope of '{method_obj.name}' method")
            exit(0)
        method_obj.add_field(field_name, field_type, is_param)

    def add_field(self, field_name, field_type):
        if field_name in self.fields:
            print(f"Field '{field_name}' is already declared in scope of '{self.name}'")
            exit(0)
        self.fields[field_name] = field_type
    
    def has_field(self, field_name):
        field_type = self.fields.get(field_name)
        if (field_type):
            return [True, self, True]
        else:
            class_object = self.search_field_in_inherited_classes(field_name)
            if class_object:
                return [True, class_object, False] 
            else:
                return [False, None, False]
    
    def get_field_type(self, field_name):
        if (self.has_field(field_name)[0]):
            return self.fields.get(field_name)

    def check_if_overide_methods_valid(self, method_object):
        method_name = method_object.get_name()
        overrided_methods = self.methods[method_name]
        method_object_types = list(method_object.get_params().values())
        for method in overrided_methods:
            if method == method_object:
                continue
            if method.get_param_number == method_object.get_param_number():
                method_types = list(method.get_params().values())
                for type in range(len(method_types)):
                    if method_types[type] != method_object_types[type]:
                        return
                print(f"All parameters are the same type within overided methods")
                exit(0)

    def search_method(self, method_name, param_num):
        methods_with_name = self.methods.get(method_name)
        
        if methods_with_name is not None:
            for method in methods_with_name:
                if method.param_number == param_num + 1:
                    return [method.version, None]
        
        inherited = self.search_method_in_inherited_classes(method_name, param_num)
        if inherited is not None:
            return inherited
        
        if method_name == self.name:
            if self.methods.get(method_name):
                return [self.methods.get(method_name)[0].version, None]
        
        print(f"Method '{method_name}' is not declared in class '{self.name}' or its parent classes")
        exit(0)
    
    def search_method_in_inherited_classes(self, method_name, param_num):
        for inherited_class in self.inherits_from:
            methods_of_class = inherited_class.methods.get(method_name)
            if methods_of_class != None:
                for method in methods_of_class:
                    if method.param_number == param_num + 1:
                        return [method.version, inherited_class]
        return None
    
    def add_inheritage_class(self, class_object):
        self.inherits_from.append(class_object)
    
    def search_field_in_inherited_classes(self, field_name):
        for inherited_class in self.inherits_from:
            if inherited_class.has_field(field_name)[0]:
                return inherited_class
        return None
    
    def __str__(self):
        inheritance_str = ', '.join([parent.name for parent in self.inherits_from])
        all_classes = [cls for classes_list in self.methods.values() for cls in classes_list]
        methods_str = '\n  '.join([str(method) for method in all_classes])
        fields_str = ', '.join([f"{name}: {type_}" for name, type_ in self.fields.items()])
        return f"Class name: {self.name}\nFields: [{fields_str}]\nInherits from: [{inheritance_str}]\nMethods:{methods_str}"


# ==========================================
#        LISTENER IMPLEMENTATION
# ==========================================

class oosMyListener(oosListener):

    def __init__(self, output_filename="out.c"):
        self.class_entries = {}
        self.output_filename = output_filename
        self.global_method_versions = {}
        self.output = []
        self.known_classes = []
        self.last_class_struct = None
        self.last_method_def = None
        self.last_method_obj = None
        self.in_constructor = False
        self.last_assignment_type = None 
        self.in_struct = False
        
        self.expression_stack = []
        self.function_stack = []
        self.function_obj_stack = []

        self.current_expression = ""
        self.boolfactor_count = 0
        self.boolterm_count = 0

        self.print_expression_list = None

        self.id_list = []
        self.types_list = []

        self.parlist = []
        self.tabs = 0
        self.function_call_param_num = 0 
        self.function_call_param_num_stack = []
        self.function_class_stack = []

    def search_actual_class_method(self, class_name, method_name, param_num):
        class_obj = self.get_class_obj(class_name)
        ver_class = class_obj.search_method(method_name, param_num)
        return ver_class

    def tabbing(self):
        return self.tabs * "\t"

    def indent(self):
        self.tabs = self.tabs + 1

    def deindent(self):
        self.tabs = self.tabs - 1

    def add_class(self, class_name):
        new = class_info(class_name)
        if isinstance(new, class_info):
            self.class_entries[new.name] = new
        return new
    
    def add_field_to_class(self, class_name, field_name, field_type):
        class_obj = self.class_entries.get(class_name)
        if (class_obj):
            class_obj.add_field(field_name, field_type)
        else:
            print("adding field to class that does not exist.")
            exit(0)

    def add_field_to_class_method(self, class_name, method_obf, field_name, field_type, is_param=False):
        class_obj = self.class_entries.get(class_name)
        if (class_obj):
            class_obj.add_field_to_method(method_obf, field_name, field_type, is_param)
        else:
            print("add_field_to_class_method to class that does not exist.")
            exit(0)

    def add_method_to_class(self, class_name, method_name, is_constructor=False, return_type=None):
        class_obj = self.class_entries.get(class_name)
        method = class_obj.add_method(method_name, is_constructor, return_type, self.global_method_versions)
        self.last_method_obj = method[1]
        return method[0]

    def get_class_obj(self, class_name):
        class_obj = self.class_entries.get(class_name)
        if class_obj is None:
            print(f"Class with class name '{class_name}' is not defined")
            exit(0)
        return class_obj

    def has_class_field(self, class_name, field_name):
        class_obj = self.get_class_obj(class_name)
        if (class_obj):
            bool_class = class_obj.has_field(field_name)
            if (bool_class[0]):
                return bool_class
            else:
                print(f"Class '{class_name}' does not have field '{field_name}' declared")
                exit(0)
    
    def get_class_field_type(self, class_name, field_name):
        return self.get_class_obj(class_name).get_field_type(field_name)
    
    def get_method_field_type(self, field_name):
        return self.last_method_obj.get_field_type(field_name)

    def chech_if_id_declared(self, id, is_self=False):
        if self.last_class_struct == "main" or is_self:
            bool_class = self.has_class_field(self.last_class_struct, id)
            if bool_class[0] == True:
                return [self.get_class_field_type(bool_class[1].name, id), bool_class[1]]
            else:
                print(f"Field with name '{id}' not declared in scope of {self.last_method_obj.get_name()}")
                exit(0)
        elif self.last_method_obj.has_field(id) == True:
            return [self.get_method_field_type(id), None]
        else:
            print(f"Field with name '{id}' not declared in scope of {self.last_method_obj.get_name()}")
            exit(0)
            
    def check_if_overide_methods_valid(self, class_name, method_object):
        class_obj = self.get_class_obj(class_name)
        class_obj.check_if_overide_methods_valid( method_object)        

    def get_oos_compiled(self):
        compiled_content = "".join(self.output)
        with open(self.output_filename, "w") as file:  
            file.write(compiled_content)
        return compiled_content
    
    def get_symb_structure(self):            
        symb_str = ""
        for class_name, class_entry in self.class_entries.items():
            symb_structure = class_entry.__str__()
            symb_str += symb_structure
            symb_str += "\n\n" + 50*"+" + "\n\n" 
        sym_filename = self.output_filename.replace('.c', '.sym')
        with open(sym_filename, "w") as file:
            file.write(symb_str)
        return symb_str

    # --------------------------------------------
    #       GRAMMAR LISTENERS
    # --------------------------------------------

    def enterStartRule(self, ctx:oosParser.StartRuleContext):
        self.output.append(f"#include <stdio.h>\n")
        self.output.append(f"#include <stdlib.h>\n")

    def enterClass_def(self, ctx:oosParser.Class_defContext):
        class_name = ctx.class_name(0).ID().getText()
        self.last_class_struct = class_name

        self.output.append(f"typedef struct {self.last_class_struct} \n{{")
        self.in_struct = True
        self.indent()
        self.known_classes.append(f"{self.last_class_struct}")
        self.output.append("\n")
        new_class = self.add_class(class_name)

        if len(ctx.class_name()) > 1:
            for class_name_ctx in ctx.class_name()[1::]:
                name = class_name_ctx.getText()
                if name in self.known_classes[:-1]:
                    new_class.add_inheritage_class(self.get_class_obj(name))
                    self.output.append(f"\t{name} {name}_parent;\n")
                else:
                    print(f"Class '{name}' not declared to be inherited from class '{self.known_classes[-1]}'. Line {ctx.start.line}")
                    exit(0)

    def exitClass_def(self, ctx:oosParser.Class_defContext):
        self.last_method_def = None

    def enterClass_body(self, ctx:oosParser.Class_bodyContext):
        self.output.append(f"}} {self.last_class_struct};\n")
        self.in_struct = False
        self.deindent()

    def enterDeclarations(self, ctx:oosParser.DeclarationsContext):
       pass
    def exitDeclarations(self, ctx:oosParser.DeclarationsContext):
        pass

    def enterDecl_line(self, ctx:oosParser.Decl_lineContext):
        if ctx.ID():
            for id in ctx.ID():
                self.id_list.append(f"{id.getText()}")

    def exitDecl_line(self, ctx:oosParser.Decl_lineContext):
        decl_type = self.types_list.pop()
        
        if decl_type != "int":
            self.output.append(f"{self.tabbing()}struct {decl_type} ")
            for id in self.id_list:
                if self.last_method_def is None or self.known_classes[-1] == "main":
                    self.add_field_to_class(self.last_class_struct, id, decl_type)
                else:
                    self.add_field_to_class_method(self.last_class_struct, self.last_method_obj, id, decl_type)
            if self.in_struct==True:
                self.id_list[:] = [f"*{id}" for id in self.id_list]
            else:
                 self.id_list[:] = [f"*{id} = NULL" for id in self.id_list]
            self.output.append(f"{", ".join(self.id_list )}")
            self.output.append(";\n")
        else:
            self.output.append(f"{self.tabbing()}{decl_type} ")
            for id in self.id_list:
                if self.last_method_def is None or self.known_classes[-1] == "main":
                    self.add_field_to_class(self.last_class_struct, id, decl_type)
                else:
                    self.add_field_to_class_method(self.last_class_struct, self.last_method_obj, id, decl_type)
            self.output.append(f"{", ".join(self.id_list)}")
            self.output.append(";\n")
        self.id_list = []

    def enterTypes(self, ctx:oosParser.TypesContext):
        if ctx.class_name():
            if (ctx.class_name().ID().getText() in self.known_classes):
                self.types_list.append(f"{ctx.class_name().ID().getText()}")
            else:
                print(f"Cannot find class '{ctx.class_name().ID().getText()}'")
                exit(0)
        elif ctx.getText() == "int":
            self.types_list.append(f"int")
    def exitTypes(self, ctx:oosParser.TypesContext):
        pass

    def enterConstructor_def(self, ctx:oosParser.Constructor_defContext):
        constructor_class_name = ctx.class_name().ID().getText()
        if constructor_class_name in self.known_classes:
            method_name = self.add_method_to_class(constructor_class_name, constructor_class_name, True)
            self.last_method_def = method_name
            self.output.append(f"{constructor_class_name}* {constructor_class_name}_{self.last_method_obj.get_version()}_init({constructor_class_name} *self_ptr")
        self.indent()
        self.in_constructor = True
        
    def exitConstructor_def(self, ctx:oosParser.Constructor_defContext):
        self.check_if_overide_methods_valid(self.known_classes[-1], self.last_method_obj)
        self.last_method_def = None
        self.output.append(f"\treturn self_ptr;\n}}\n")
        self.in_constructor = False
        self.deindent()
   
    def enterParlist(self, ctx:oosParser.ParlistContext):
        if ctx.ID():
            for id in ctx.ID():
                self.parlist.append(f"{id.getText()}")

    def exitParlist(self, ctx:oosParser.ParlistContext):
        for idx in range(len(self.types_list)):
            if self.types_list[idx] != "int":   
                self.add_field_to_class_method(self.known_classes[-1], self.last_method_obj, self.parlist[idx], self.types_list[idx], True)
                self.output.append(f", {self.types_list[idx]} *{self.parlist[idx]}")
            else:
                self.add_field_to_class_method(self.known_classes[-1], self.last_method_obj, self.parlist[idx], "int", True)
                self.output.append(f", {self.types_list[idx]} {self.parlist[idx]}")
        self.parlist = []
        self.types_list = []
        self.output.append(f")\n{{\n")
        
        if self.in_constructor:
            self.output.append(f"\tif(self_ptr == NULL)\n")
            self.indent()
            self.output.append(f"{self.tabbing()}{{\n")
            self.output.append(f"\t\tself_ptr = ({self.last_class_struct} *)malloc(sizeof({self.last_class_struct}));\n")
            self.output.append(f"{self.tabbing()}}}\n")
            self.deindent()

    def enterMethod_def(self, ctx:oosParser.Method_defContext):
        method_name = ctx.ID().getText()
        self.last_method_def = method_name
        ret = ctx.getChild(4).getText()
        return_type = ""
        self.indent()

        if "int" in ret:
            return_type = "int"
        elif "-" in ret:
            return_type = "void"
        elif ctx.class_name() is not None:
            class_name = ctx.class_name().getText()
            self.get_class_obj(class_name) 
            return_type = class_name

        self.add_method_to_class(self.known_classes[-1], method_name, False, return_type)
        if "int" not in return_type and "void" not in return_type:
            return_type = return_type +"*"

        self.output.append(f"{return_type} {method_name}_{self.last_method_obj.get_version()}({self.known_classes[-1]} *self_ptr")
        self.last_method_def = method_name

    def exitMethod_def(self, ctx:oosParser.Method_defContext):
        self.check_if_overide_methods_valid(self.known_classes[-1], self.last_method_obj)
        self.deindent()
        self.output.append(f"}}\n")

    def enterClass_main_def(self, ctx:oosParser.Method_main_defContext):
        self.last_class_struct = "main"
        self.known_classes.append("main")
        self.add_class("main")
        self.output.append(f"int main(void)\n{{\n")
        self.indent()
        
    def exitClass_main_def(self, ctx:oosParser.Method_main_defContext):
        self.output.append(f"\treturn 0;\n}}")
        
    def enterStatement(self, ctx:oosParser.StatementContext):
        pass    
    def exitStatement(self, ctx:oosParser.StatementContext):
        if (ctx.getChildCount()):
            self.output.append(f"\n")           

    def enterReturn_stat(self, ctx:oosParser.Return_statContext):
        self.output.append(f"\treturn ")
        if ctx.expression():
            self.last_assignment_type = self.last_method_obj.get_return_type()
        elif ctx.getChildCount() == 2 and ctx.getChild(1).getText() == "self":
            self.output.append(f"self_ptr") 
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "self.":
            id = ctx.ID().getText()
            type_class = self.chech_if_id_declared(id, True)
            if (type_class[0] != self.last_method_obj.get_return_type()):
                print(f"Incompatible type")
                exit()
            if type_class[1].name != self.known_classes[-1]:
                id = f"{type_class[1].name}_parent.{id}"
            self.output.append(f"self_ptr->{id}") 

    def exitReturn_stat(self, ctx:oosParser.Return_statContext):
        self.output.append(f";")

    def enterAssignment_stat(self, ctx:oosParser.Assignment_statContext):     
        if "self." in ctx.getText().split('=')[0] and self.last_class_struct != "main":
            class_self, assign = ctx.getText().split('.',1)
            field, val = assign.split('=')
            bool_class = self.has_class_field(self.known_classes[-1], field)
            if (bool_class[0]):
                type_class = self.chech_if_id_declared(field, True)
                self.last_assignment_type = type_class[0]
                if type_class[1].name != self.known_classes[-1]:
                    field = f"{type_class[1].name}_parent.{field}"
                self.function_obj_stack.append((f"self_ptr->{field}", self.last_assignment_type)) 
                self.output.append(f"\tself_ptr->{field} = ")
        elif ctx.ID:
            id = str(ctx.ID())
            self.last_assignment_type = self.chech_if_id_declared(id)[0]
            self.function_obj_stack.append((id, self.last_assignment_type)) 
            self.output.append(f"\t{id} = ")
   
    def exitAssignment_stat(self, ctx:oosParser.Assignment_statContext):
        self.output.append(f";")
        self.last_assignment_type = None
        self.function_obj_stack = []

    def enterExpression(self, ctx:oosParser.ExpressionContext):
        self.expression_stack.append("")
 
    def exitExpression(self, ctx:oosParser.ExpressionContext):
        completed_expression = self.expression_stack.pop()
        if self.expression_stack:
            self.expression_stack[-1] += completed_expression
        else:
            self.current_expression = completed_expression
            if self.print_expression_list == None:
                self.output.append(self.current_expression)
            else:
                self.print_expression_list.append(self.current_expression)
            
    def enterFactor(self, ctx:oosParser.FactorContext):
        current_expr = self.expression_stack[-1] if self.expression_stack else ""
       
        if ctx.INTEGER():
            current_expr += f"{ctx.getText()}"
        
        elif ctx.expression():
            current_expr += f"("
        
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "self." and ctx.ID():
            field = str(ctx.getChild(1).getText())
            if (self.has_class_field(self.known_classes[-1], field)[0] and self.last_class_struct != "main"):
                tmp_class = self.has_class_field( self.known_classes[-1], field)[1]
                if tmp_class.name != self.known_classes[-1]:
                    field = f"{tmp_class.name}_parent.{field}"
                current_expr += f"self_ptr->{field}" 
            else:
                current_expr += f"{field}"

        elif ctx.getChildCount() == 1 and ctx.ID():
            current_expr += f"{str(ctx.ID(0))}"
        
        elif ctx.getChildCount() == 4 and ctx.getChild(0).getText() == "self." and ctx.getChild(2).getText() == "." and ctx.ID() and ctx.func_call():
            id = str(ctx.getChild(1).getText())
            bool_class = self.has_class_field(self.known_classes[-1], id)
            type_class = self.chech_if_id_declared(id, True)
            #print(f"[DEBUG enterFactor self.id.function] id: {id}, type_class: {type_class}")
            if (bool_class[0]):    
                field_access = id
                if type_class[1].name != self.known_classes[-1]:
                    field_access = f"{type_class[1].name}_parent.{id}"
                #print(f"[DEBUG enterFactor self.id.function] Pushing (self$ -> {field_access}, {type_class[0]})")
                self.function_obj_stack.append((f"self_ptr->{field_access}", type_class[0]))
            else:
                #print(f"[DEBUG enterFactor self.id.function] Field not found")
                self.function_obj_stack.append((f"self_ptr->{id}", type_class[0]))
        
        elif ctx.getChildCount() >= 3 and ctx.getChild(1).getText() == '.' and ctx.ID and ctx.func_call():
            id = str(ctx.getChild(0).getText())
            type = self.chech_if_id_declared(id)[0]
            #print(f"[DEBUG enterFactor id.function] id: {id}, type: {type}")
            self.function_obj_stack.append((id, type))
            
        elif ctx.func_call():
            is_self = False
            if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "self.":
                is_self = True
            
            if is_self:
                #print(f"[DEBUG enterFactor func_call] Pushing (self$, {self.known_classes[-1]})")
                self.function_obj_stack.append(("self_ptr", self.known_classes[-1]))
            else:
                func_name = ctx.func_call().ID().getText()
                if func_name in self.known_classes:
                    #print(f"[DEBUG enterFactor func_call] Constructor {func_name}, Pushing (NULL, {func_name})")
                    self.function_obj_stack.append(("NULL", func_name)) 
                else:
                    self.function_obj_stack.append(("self_ptr", self.known_classes[-1]))

        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '.':
            class_id = ctx.getChild(0).getText() 
            field_id = ctx.getChild(2).getText() 
            class_id_type = self.chech_if_id_declared(class_id)[0]
            if (self.has_class_field( class_id_type, field_id)[0] or self.print_expression_list != None):
                tmp_class = self.has_class_field( class_id_type, field_id) 
                if tmp_class[1].name != self.known_classes[-1] and tmp_class[2] == False:
                    field_id = f"{tmp_class[1].name}_parent.{field_id}"
                current_expr += f"{class_id}->{field_id}" 

        if self.expression_stack:
            self.expression_stack[-1] = current_expr
            
    def exitFactor(self, ctx:oosParser.FactorContext):
       if ctx.expression():
            self.expression_stack[-1] += ")"
    
    def enterFunc_call(self, ctx:oosParser.Func_callContext):
        function_name = ctx.ID().getText()
        if self.function_call_param_num > 0:
            self.function_call_param_num_stack.append(self.function_call_param_num)
            self.function_call_param_num = 0
        
        if (self.function_obj_stack != []):
            id, type = self.function_obj_stack.pop()
            self.function_class_stack.append(type)
            self.function_stack.append(f"{function_name}({id}")

    def exitFunc_call(self, ctx:oosParser.Func_callContext):
        if self.function_stack:
            function_call = self.function_stack.pop()
            class_name_of_object = self.function_class_stack.pop() 
            
            parts = function_call.split('(', 1)
            function_name = parts[0].strip()
            arguments = parts[1].strip() 
            rest_args = ""
            
            if ',' in arguments:
                rest_args = ", " + arguments.split(',', 1)[1]
            
            object_param = arguments.split(',')[0].split(')')[0].strip()
            
            is_constructor = function_name in self.known_classes
            #print(f"[DEBUG exitFunc_call] function_name: {function_name}, class_name_of_object: {class_name_of_object}, is_constructor: {is_constructor}, object_param: {object_param}")
            ver_info = self.search_actual_class_method(class_name_of_object, function_name, self.function_call_param_num)
            version = ver_info[0]
            inherited_class_obj = ver_info[1]
            #print(f"[DEBUG exitFunc_call] version: {version}, inherited_class_obj: {inherited_class_obj}")

            c_first_arg = ""
            
            if is_constructor:
                if "->" in object_param:
                    c_first_arg = object_param
                else:
                    c_first_arg = object_param
            else:
                if object_param == "self_ptr":  
                    c_first_arg = "self_ptr" 
                elif "->" in object_param: 
                    c_first_arg = object_param 
                elif object_param == "NULL":
                    c_first_arg = "NULL"
                else:
                    c_first_arg = object_param

            if inherited_class_obj is not None and not is_constructor:
                 if "->" in c_first_arg:
                     c_first_arg = f"&{c_first_arg}.{inherited_class_obj.name}_parent"
                 elif c_first_arg == "self_ptr": 
                     c_first_arg = f"&self_ptr->{inherited_class_obj.name}_parent"
                 else:
                     c_first_arg = f"&{c_first_arg}->{inherited_class_obj.name}_parent"

            final_c_func_name = ""
            if is_constructor:
                final_c_func_name = f"{function_name}_{version}_init"
            else:
                final_c_func_name = f"{function_name}_{version}"

            final_args = c_first_arg + rest_args
            function_call = f"{final_c_func_name}({final_args})"
            #print(f"[DEBUG exitFunc_call] FINAL: {function_call}")
            if self.expression_stack:
                self.expression_stack[-1] += function_call
            else:
                self.current_expression = function_call

        if len(self.function_call_param_num_stack):
            self.function_call_param_num = self.function_call_param_num_stack.pop()
        else:
            self.function_call_param_num = 0

    def enterArglist(self, ctx:oosParser.ArglistContext):
        if(ctx.argitem()):
            self.expression_stack.append("")
    
    def enterArgitem(self, ctx:oosParser.ArgitemContext):
        if (ctx.expression()):
            self.function_call_param_num += 1
            self.expression_stack[-1] +=", "

    def exitArgitem(self, ctx:oosParser.ArgitemContext):
        pass

    def exitArglist(self, ctx:oosParser.ArglistContext):
        if(ctx.argitem()):
            if self.expression_stack:
                completed_expression = self.expression_stack.pop()
                self.function_stack[-1] += completed_expression
               
    def enterDirect_call_stat(self, ctx:oosParser.Direct_call_statContext):
        if ctx.getChildCount() >= 3 and ctx.getChild(1).getText() == '.' and ctx.ID() and ctx.func_call():
            id = str(ctx.ID())
            type = self.chech_if_id_declared(id)[0]
            self.function_obj_stack.append((id, type))
        
        elif ctx.getChildCount() == 4 and ctx.getChild(0).getText() == "self." and ctx.getChild(2).getText() == "." and ctx.ID() and ctx.func_call():
            id = str(ctx.getChild(1).getText())
            bool_class = self.has_class_field(self.known_classes[-1], id)
            if (bool_class[0]):
                type_class = self.chech_if_id_declared(id, True)
                self.last_assignment_type = type_class[0]
                if type_class[1].name != self.known_classes[-1]:
                    id = f"{type_class[1].name}_parent.{id}"
                self.function_obj_stack.append((f"self_ptr->{id}", self.last_assignment_type)) 
        
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "self." and ctx.func_call():
            self.function_obj_stack.append(("self_ptr", self.known_classes[-1]))

        elif ctx.getChildCount() == 1 and ctx.func_call():
            func_name = ctx.func_call().ID().getText()
            if func_name in self.known_classes:
                self.function_obj_stack.append(("NULL", func_name)) 
            else:
                self.function_obj_stack.append(("self_ptr", self.known_classes[-1]))

    def exitDirect_call_stat(self, ctx:oosParser.Direct_call_statContext):
        self.output.append(f"\t{self.current_expression};")

    def enterPrint_stat(self, ctx:oosParser.Print_statContext):
        self.print_expression_list = []
        self.output.append(f"\tprintf(\"")

    def exitPrint_stat(self, ctx:oosParser.Print_statContext):
        fields=""
        formating = ""
        #print(f"[DEBUG] print_expression_list: {self.print_expression_list}")

        for expression in self.print_expression_list:
            fields += "%d "
            formating += str(", ")+expression
        #print(f"[DEBUG] Final printf: printf(\"{fields}\\n\"{formating});")
        
        self.output.append(f"{fields}\\n\"{formating});")
        self.print_expression_list = None

    def enterInput_stat(self, ctx:oosParser.Input_statContext):
        id = None
        type = None
        if ctx.getChildCount() == 2 and ctx.ID:
            id = ctx.ID().getText()
            type = self.chech_if_id_declared(id)[0]
        elif ctx.getChildCount() == 3 and ctx.ID:
            id = ctx.ID().getText()
            type = self.chech_if_id_declared(id, True)[0]
            if self.last_class_struct != "main":
                id = "self_ptr->" + id
        if (type != "int"):
            print(f"You are trying to input on an 'Object' type which is illegal . Line {ctx.start.line}")
            exit(0)
        self.output.append(f"\tscanf(\"%d\", &{id})")
    def exitInput_stat(self, ctx:oosParser.Input_statContext):
        pass

    def enterCondition(self, ctx:oosParser.ConditionContext):
        self.boolterm_count = len(ctx.boolterm()) - 1
    def exitCondition(self, ctx:oosParser.ConditionContext):
        self.output.append(f")\n{{\n")
        self.indent()

    def enterBoolterm(self, ctx:oosParser.BooltermContext):
        self.boolfactor_count = len(ctx.boolfactor()) - 1
    def exitBoolterm(self, ctx:oosParser.BooltermContext):
        if self.boolterm_count > 0:
            self.output.append(" || ")
            self.boolfactor_count -= 1 
    
    def enterBoolfactor(self, ctx:oosParser.BoolfactorContext):
        if ctx.getChildCount() == 4 and ctx.getChild(0).getText() == 'not':
            self.output.append("!(") 
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '[':
            self.output.append("(")
        elif ctx.expression(0) and ctx.rel_oper() and ctx.expression(1):
            pass
    def exitBoolfactor(self, ctx:oosParser.BoolfactorContext):
        if self.boolfactor_count > 0:
            self.output.append(" && ")
            self.boolfactor_count -= 1
        if ctx.getChildCount() in [3, 4] and ctx.getChild(0).getText() in ['not', '[']:
            self.output.append(")")

    def enterWhile_stat(self, ctx:oosParser.While_statContext):
        self.output.append(f"\n\twhile(")
    def exitWhile_stat(self, ctx:oosParser.While_statContext):
        self.deindent()
        self.output.append(f"\t}}")

    def enterIf_stat(self, ctx:oosParser.If_statContext):
        self.output.append(f"\n\tif(")
    def exitIf_stat(self, ctx:oosParser.If_statContext):
        self.output.append(f"\n")
        
    def enterElse_part(self, ctx:oosParser.Else_partContext):
        self.deindent()
        self.output.append(f"\t}}")
        if (ctx.statements()):
            self.output.append(f"\n\telse\n\t{{\n")
            self.indent()
    def exitElse_part(self, ctx:oosParser.Else_partContext):
        if (ctx.statements()):
            self.deindent()
            self.output.append(f"\t}}")

    def enterRel_oper(self, ctx:oosParser.Rel_operContext):
        if ctx.getChildCount() > 0:
            self.output.append(f" {ctx.getText()} ")
    def enterAdd_oper(self, ctx:oosParser.Add_operContext):
        if self.expression_stack:
            self.expression_stack[-1] += (f" {ctx.getText()} ")
    def enterMul_oper(self, ctx:oosParser.Mul_operContext):
        if self.expression_stack:
            self.expression_stack[-1] += (f" {ctx.getText()} ")