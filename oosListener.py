# Generated from oos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .oosParser import oosParser
else:
    from oosParser import oosParser

# This class defines a complete listener for a parse tree produced by oosParser.
class oosListener(ParseTreeListener):

    # Enter a parse tree produced by oosParser#startRule.
    def enterStartRule(self, ctx:oosParser.StartRuleContext):
        pass

    # Exit a parse tree produced by oosParser#startRule.
    def exitStartRule(self, ctx:oosParser.StartRuleContext):
        pass


    # Enter a parse tree produced by oosParser#classes.
    def enterClasses(self, ctx:oosParser.ClassesContext):
        pass

    # Exit a parse tree produced by oosParser#classes.
    def exitClasses(self, ctx:oosParser.ClassesContext):
        pass


    # Enter a parse tree produced by oosParser#class_def.
    def enterClass_def(self, ctx:oosParser.Class_defContext):
        pass

    # Exit a parse tree produced by oosParser#class_def.
    def exitClass_def(self, ctx:oosParser.Class_defContext):
        pass


    # Enter a parse tree produced by oosParser#class_main_def.
    def enterClass_main_def(self, ctx:oosParser.Class_main_defContext):
        pass

    # Exit a parse tree produced by oosParser#class_main_def.
    def exitClass_main_def(self, ctx:oosParser.Class_main_defContext):
        pass


    # Enter a parse tree produced by oosParser#class_name.
    def enterClass_name(self, ctx:oosParser.Class_nameContext):
        pass

    # Exit a parse tree produced by oosParser#class_name.
    def exitClass_name(self, ctx:oosParser.Class_nameContext):
        pass


    # Enter a parse tree produced by oosParser#declarations.
    def enterDeclarations(self, ctx:oosParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by oosParser#declarations.
    def exitDeclarations(self, ctx:oosParser.DeclarationsContext):
        pass


    # Enter a parse tree produced by oosParser#class_body.
    def enterClass_body(self, ctx:oosParser.Class_bodyContext):
        pass

    # Exit a parse tree produced by oosParser#class_body.
    def exitClass_body(self, ctx:oosParser.Class_bodyContext):
        pass


    # Enter a parse tree produced by oosParser#main_body.
    def enterMain_body(self, ctx:oosParser.Main_bodyContext):
        pass

    # Exit a parse tree produced by oosParser#main_body.
    def exitMain_body(self, ctx:oosParser.Main_bodyContext):
        pass


    # Enter a parse tree produced by oosParser#decl_line.
    def enterDecl_line(self, ctx:oosParser.Decl_lineContext):
        pass

    # Exit a parse tree produced by oosParser#decl_line.
    def exitDecl_line(self, ctx:oosParser.Decl_lineContext):
        pass


    # Enter a parse tree produced by oosParser#constructor_def.
    def enterConstructor_def(self, ctx:oosParser.Constructor_defContext):
        pass

    # Exit a parse tree produced by oosParser#constructor_def.
    def exitConstructor_def(self, ctx:oosParser.Constructor_defContext):
        pass


    # Enter a parse tree produced by oosParser#method_def.
    def enterMethod_def(self, ctx:oosParser.Method_defContext):
        pass

    # Exit a parse tree produced by oosParser#method_def.
    def exitMethod_def(self, ctx:oosParser.Method_defContext):
        pass


    # Enter a parse tree produced by oosParser#method_main_def.
    def enterMethod_main_def(self, ctx:oosParser.Method_main_defContext):
        pass

    # Exit a parse tree produced by oosParser#method_main_def.
    def exitMethod_main_def(self, ctx:oosParser.Method_main_defContext):
        pass


    # Enter a parse tree produced by oosParser#types.
    def enterTypes(self, ctx:oosParser.TypesContext):
        pass

    # Exit a parse tree produced by oosParser#types.
    def exitTypes(self, ctx:oosParser.TypesContext):
        pass


    # Enter a parse tree produced by oosParser#parameters.
    def enterParameters(self, ctx:oosParser.ParametersContext):
        pass

    # Exit a parse tree produced by oosParser#parameters.
    def exitParameters(self, ctx:oosParser.ParametersContext):
        pass


    # Enter a parse tree produced by oosParser#method_body.
    def enterMethod_body(self, ctx:oosParser.Method_bodyContext):
        pass

    # Exit a parse tree produced by oosParser#method_body.
    def exitMethod_body(self, ctx:oosParser.Method_bodyContext):
        pass


    # Enter a parse tree produced by oosParser#return_type.
    def enterReturn_type(self, ctx:oosParser.Return_typeContext):
        pass

    # Exit a parse tree produced by oosParser#return_type.
    def exitReturn_type(self, ctx:oosParser.Return_typeContext):
        pass


    # Enter a parse tree produced by oosParser#parlist.
    def enterParlist(self, ctx:oosParser.ParlistContext):
        pass

    # Exit a parse tree produced by oosParser#parlist.
    def exitParlist(self, ctx:oosParser.ParlistContext):
        pass


    # Enter a parse tree produced by oosParser#statements.
    def enterStatements(self, ctx:oosParser.StatementsContext):
        pass

    # Exit a parse tree produced by oosParser#statements.
    def exitStatements(self, ctx:oosParser.StatementsContext):
        pass


    # Enter a parse tree produced by oosParser#statement.
    def enterStatement(self, ctx:oosParser.StatementContext):
        pass

    # Exit a parse tree produced by oosParser#statement.
    def exitStatement(self, ctx:oosParser.StatementContext):
        pass


    # Enter a parse tree produced by oosParser#assignment_stat.
    def enterAssignment_stat(self, ctx:oosParser.Assignment_statContext):
        pass

    # Exit a parse tree produced by oosParser#assignment_stat.
    def exitAssignment_stat(self, ctx:oosParser.Assignment_statContext):
        pass


    # Enter a parse tree produced by oosParser#direct_call_stat.
    def enterDirect_call_stat(self, ctx:oosParser.Direct_call_statContext):
        pass

    # Exit a parse tree produced by oosParser#direct_call_stat.
    def exitDirect_call_stat(self, ctx:oosParser.Direct_call_statContext):
        pass


    # Enter a parse tree produced by oosParser#if_stat.
    def enterIf_stat(self, ctx:oosParser.If_statContext):
        pass

    # Exit a parse tree produced by oosParser#if_stat.
    def exitIf_stat(self, ctx:oosParser.If_statContext):
        pass


    # Enter a parse tree produced by oosParser#else_part.
    def enterElse_part(self, ctx:oosParser.Else_partContext):
        pass

    # Exit a parse tree produced by oosParser#else_part.
    def exitElse_part(self, ctx:oosParser.Else_partContext):
        pass


    # Enter a parse tree produced by oosParser#while_stat.
    def enterWhile_stat(self, ctx:oosParser.While_statContext):
        pass

    # Exit a parse tree produced by oosParser#while_stat.
    def exitWhile_stat(self, ctx:oosParser.While_statContext):
        pass


    # Enter a parse tree produced by oosParser#return_stat.
    def enterReturn_stat(self, ctx:oosParser.Return_statContext):
        pass

    # Exit a parse tree produced by oosParser#return_stat.
    def exitReturn_stat(self, ctx:oosParser.Return_statContext):
        pass


    # Enter a parse tree produced by oosParser#input_stat.
    def enterInput_stat(self, ctx:oosParser.Input_statContext):
        pass

    # Exit a parse tree produced by oosParser#input_stat.
    def exitInput_stat(self, ctx:oosParser.Input_statContext):
        pass


    # Enter a parse tree produced by oosParser#print_stat.
    def enterPrint_stat(self, ctx:oosParser.Print_statContext):
        pass

    # Exit a parse tree produced by oosParser#print_stat.
    def exitPrint_stat(self, ctx:oosParser.Print_statContext):
        pass


    # Enter a parse tree produced by oosParser#expression.
    def enterExpression(self, ctx:oosParser.ExpressionContext):
        pass

    # Exit a parse tree produced by oosParser#expression.
    def exitExpression(self, ctx:oosParser.ExpressionContext):
        pass


    # Enter a parse tree produced by oosParser#arguments.
    def enterArguments(self, ctx:oosParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by oosParser#arguments.
    def exitArguments(self, ctx:oosParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by oosParser#condition.
    def enterCondition(self, ctx:oosParser.ConditionContext):
        pass

    # Exit a parse tree produced by oosParser#condition.
    def exitCondition(self, ctx:oosParser.ConditionContext):
        pass


    # Enter a parse tree produced by oosParser#optional_sign.
    def enterOptional_sign(self, ctx:oosParser.Optional_signContext):
        pass

    # Exit a parse tree produced by oosParser#optional_sign.
    def exitOptional_sign(self, ctx:oosParser.Optional_signContext):
        pass


    # Enter a parse tree produced by oosParser#term.
    def enterTerm(self, ctx:oosParser.TermContext):
        pass

    # Exit a parse tree produced by oosParser#term.
    def exitTerm(self, ctx:oosParser.TermContext):
        pass


    # Enter a parse tree produced by oosParser#add_oper.
    def enterAdd_oper(self, ctx:oosParser.Add_operContext):
        pass

    # Exit a parse tree produced by oosParser#add_oper.
    def exitAdd_oper(self, ctx:oosParser.Add_operContext):
        pass


    # Enter a parse tree produced by oosParser#arglist.
    def enterArglist(self, ctx:oosParser.ArglistContext):
        pass

    # Exit a parse tree produced by oosParser#arglist.
    def exitArglist(self, ctx:oosParser.ArglistContext):
        pass


    # Enter a parse tree produced by oosParser#boolterm.
    def enterBoolterm(self, ctx:oosParser.BooltermContext):
        pass

    # Exit a parse tree produced by oosParser#boolterm.
    def exitBoolterm(self, ctx:oosParser.BooltermContext):
        pass


    # Enter a parse tree produced by oosParser#factor.
    def enterFactor(self, ctx:oosParser.FactorContext):
        pass

    # Exit a parse tree produced by oosParser#factor.
    def exitFactor(self, ctx:oosParser.FactorContext):
        pass


    # Enter a parse tree produced by oosParser#mul_oper.
    def enterMul_oper(self, ctx:oosParser.Mul_operContext):
        pass

    # Exit a parse tree produced by oosParser#mul_oper.
    def exitMul_oper(self, ctx:oosParser.Mul_operContext):
        pass


    # Enter a parse tree produced by oosParser#argitem.
    def enterArgitem(self, ctx:oosParser.ArgitemContext):
        pass

    # Exit a parse tree produced by oosParser#argitem.
    def exitArgitem(self, ctx:oosParser.ArgitemContext):
        pass


    # Enter a parse tree produced by oosParser#boolfactor.
    def enterBoolfactor(self, ctx:oosParser.BoolfactorContext):
        pass

    # Exit a parse tree produced by oosParser#boolfactor.
    def exitBoolfactor(self, ctx:oosParser.BoolfactorContext):
        pass


    # Enter a parse tree produced by oosParser#func_call.
    def enterFunc_call(self, ctx:oosParser.Func_callContext):
        pass

    # Exit a parse tree produced by oosParser#func_call.
    def exitFunc_call(self, ctx:oosParser.Func_callContext):
        pass


    # Enter a parse tree produced by oosParser#constructor_call.
    def enterConstructor_call(self, ctx:oosParser.Constructor_callContext):
        pass

    # Exit a parse tree produced by oosParser#constructor_call.
    def exitConstructor_call(self, ctx:oosParser.Constructor_callContext):
        pass


    # Enter a parse tree produced by oosParser#rel_oper.
    def enterRel_oper(self, ctx:oosParser.Rel_operContext):
        pass

    # Exit a parse tree produced by oosParser#rel_oper.
    def exitRel_oper(self, ctx:oosParser.Rel_operContext):
        pass



del oosParser