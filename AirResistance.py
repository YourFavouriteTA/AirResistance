

from manimlib.imports import *
import os
import pyclbr

global  speedcolor
global  carcolor
global  dragcolor

speedcolor=BLUE
carcolor=GREEN
dragcolor=RED

class Intro(Scene):
    def construct(self):
        
        Maintext=TextMobject("Physics in action!")
        Maintext.scale(2)
        Maintext.move_to(UP)
        belowtext=TextMobject("Newton's 2nd law and separation of variables")
        belowtext.next_to(Maintext,2*DOWN)
        title=VGroup(Maintext,belowtext)
        self.wait(0.5)
        self.play(Write(title))
        self.wait(4)        
        
class Setup(Scene):
    def construct(self):


        
        Text1=TextMobject("Imagine a ","{car}"," with ","{speed $\\bar{v}$}"," being slowed down by ","{air resistance}",".")
        Text1.set_color_by_tex_to_color_map({
            "{car}": carcolor, "{speed $\\bar{v}$}":speedcolor,"{air resistance}": dragcolor})
        self.play(Write(Text1))
        self.wait(1.5)
        self.play(ApplyMethod(Text1.to_edge,UP))
        self.wait()

        carheight=1
        carwidth=3
        #Make car
        rectangle = Rectangle(height=carheight, width=carwidth,color=carcolor)
        #rectangle.to_edge(LEFT)
        wheel1=Circle(radius=0.4,color=carcolor)
        wheel2=Circle(radius=0.4,color=carcolor)
        wheel1.move_to(rectangle.get_center()+DOWN*carheight/2+RIGHT)
        wheel2.move_to(rectangle.get_center()+DOWN*carheight/2+LEFT)
        self.play(ShowCreation(rectangle),ShowCreation(wheel1),ShowCreation(wheel2))
        
        
        #Define vectors
        speedlabel=TexMobject("\\vec{v}",color=speedcolor)
        draglabel=TexMobject("\\vec{F_d}","=-c","\\vec{v}")
        draglabel.set_color_by_tex_to_color_map({
            "{F_d}": dragcolor,
            "{v}":speedcolor})
        
        
    
        speedarrow=Arrow(rectangle.get_center()+np.array([1.5,0,0]),rectangle.get_center()+np.array([4,0,0]),color=speedcolor)
        dragarrow=Arrow(rectangle.get_center()+np.array([-1.5,0,0]),rectangle.get_center()+np.array([-4,0,0]),color=dragcolor)
    
        speedlabel.next_to(speedarrow,UP)
        draglabel.next_to(dragarrow,UP)
        
        self.play(ShowCreation(speedarrow),ShowCreation(dragarrow),Write(speedlabel),Write(draglabel))
        self.wait(1.5)
        Text2=TextMobject("More ","{speed}"," means more ","{air resistance}")
        Text2.set_color_by_tex_to_color_map({
            "{car}": carcolor, "{speed}":speedcolor,"{air resistance}": dragcolor})
        Text2.move_to(Text1)
        self.play(ReplacementTransform(Text1,Text2))
        self.wait(1.5)
        speedarrow2=Arrow(rectangle.get_center()+np.array([1.5,0,0]),rectangle.get_center()+np.array([6,0,0]),color=speedcolor)
        dragarrow2=Arrow(rectangle.get_center()+np.array([-1.5,0,0]),rectangle.get_center()+np.array([-6,0,0]),color=dragcolor)

        speedarrow3=Arrow(rectangle.get_center()+np.array([1.5,0,0]),rectangle.get_center()+np.array([4,0,0]),color=speedcolor)
        dragarrow3=Arrow(rectangle.get_center()+np.array([-1.5,0,0]),rectangle.get_center()+np.array([-4,0,0]),color=dragcolor)


        self.play(Transform(speedarrow,speedarrow2),Transform(dragarrow,dragarrow2))
        self.wait(1.5)
        self.play(Transform(speedarrow,speedarrow3),Transform(dragarrow,dragarrow3))
        self.wait(1.5)
        questiontext=TexMobject("\\text{How does }","\\vec{v}","\\text{ change with time?}")
        questiontext.set_color_by_tex_to_color_map({
            "{v}": speedcolor})
        questiontext.move_to(rectangle.get_center())
        rectangle = Rectangle(height=0.75, width=7,fill_color=BLACK, fill_opacity=1, color=GOLD_A)
        rectangle.move_to(rectangle.get_center())
        self.play(ShowCreation(rectangle),Write(questiontext),run_time=3)
          
        
        
        
        
        
        self.wait(3)
        
   
class N2(Scene):
    def construct(self):

#        middleline=Line(np.array([0,-3,0]),np.array([0,3,0]))
#        horzline=Line(np.array([-6,-2.0,0]),np.array([6,-2.0,0]))
#        self.add(middleline)
#        self.add(horzline)
        carheight=1
        carwidth=3
        #Make car
        rectangle = Rectangle(height=carheight, width=carwidth,color=carcolor)
        rectangle.to_edge(DOWN)
        wheel1=Circle(radius=0.4,color=carcolor)
        wheel2=Circle(radius=0.4,color=carcolor)
        wheel1.move_to(rectangle.get_center()+DOWN*carheight/2+RIGHT)
        wheel2.move_to(rectangle.get_center()+DOWN*carheight/2+LEFT)
        self.play(ShowCreation(rectangle),ShowCreation(wheel1),ShowCreation(wheel2))
        
        
        #Define vectors
        speedlabel=TexMobject("\\vec{v}",color=speedcolor)
        draglabel=TexMobject("\\vec{F_d}","=-c","\\vec{v}")
        draglabel.set_color_by_tex_to_color_map({
            "{F_d}": dragcolor,
            "{v}":speedcolor})
        
        
    
        speedarrow=Arrow(rectangle.get_center()+np.array([1.5,0,0]),rectangle.get_center()+np.array([4,0,0]),color=speedcolor)
        dragarrow=Arrow(rectangle.get_center()+np.array([-1.5,0,0]),rectangle.get_center()+np.array([-4,0,0]),color=dragcolor)
    
        speedlabel.next_to(speedarrow,UP)
        draglabel.next_to(dragarrow,UP)
        
        self.play(ShowCreation(speedarrow),ShowCreation(dragarrow),Write(speedlabel),Write(draglabel))


        Headtext=TextMobject("Newton's 2nd law:")
        Headtext.move_to(3*UP+3.5*LEFT)
        N2eq1=TexMobject("\\sum \\vec{F} = m \\vec{a}")
        N2eq1.next_to(Headtext,DOWN)
        
        
        N2eq2=TexMobject("{\\vec{F_d}}","= m \\vec{a} ")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq2.next_to(N2eq1,DOWN)
        N2eq2.set_color_by_tex_to_color_map({
            "{F_d}": dragcolor})
        
        
        N2eq3=TexMobject("-c","\\vec{v}","= m ","{d ","\\vec{v}","\\over dt","} ")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq3.next_to(N2eq2,DOWN)
        N2eq3.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        N2eq4=TexMobject("-c","{v}","\\hat{x}= m\\hat{x}","{d ","{v}","\\over dt","} ")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq4.next_to(N2eq2,DOWN)
        N2eq4.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        N2eq5=TexMobject("-c","{v}","= m","{d ","{v}","\\over dt","} ")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq5.next_to(N2eq2,DOWN)
        N2eq5.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        N2eq6=TexMobject("m","{d ","{v}","\\over dt","} ","=-c","{v}")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq6.next_to(N2eq2,DOWN)
        N2eq6.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        N2eq7=TexMobject("{d ","{v}","\\over dt","} ","=- \\frac{c}{m} ","{v}")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq7.next_to(N2eq2,DOWN)
        N2eq7.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        
        
        
        
       
        
        
        
        
        
        
        self.play(Write(Headtext), Write(N2eq1)) #N2 draws on screen
        self.wait(5) #"It says: How much the ball changes its speed depends on all the forces acting on it"
        self.play(Write(N2eq2))
        self.wait(5)# The Gravity and Drag on the ball are given by these expressions
        self.play(Write(N2eq3))
        self.wait(5)# Let us write the vectors as the product of their magnitude and directions
        self.play(Transform(N2eq3,N2eq4))
        self.wait(5)#Let us look only at the magnitudes since they are all in the y-direction 
        self.play(Transform(N2eq3,N2eq5))
        self.wait(2)#Rearrange this to isolate the derivative
        self.play(Transform(N2eq3,N2eq6))
        self.wait(3)
        self.play(Transform(N2eq3,N2eq7))
        self.wait(2) #Let us tidy things up a bit
#       

        solvetext=TextMobject("Separate variables!")
        solvetext.move_to(3*UP+3.5*RIGHT)
        N2eq8=TexMobject("{d ","{v}","\\over dt}","=-\\frac{c}{m} ","{v}")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq8.next_to(solvetext,DOWN)
        N2eq8.set_color_by_tex_to_color_map({
            "{v}": BLUE})
        
        
        N2eq9=TexMobject("{d ","{v}","\\over ","{v}","}=- \\frac{c}{m} dt")#= m \\frac{d\\vec{v}}{dt^2} 
        N2eq9.next_to(N2eq8,DOWN)
        N2eq9.set_color_by_tex_to_color_map({
            "{v}": speedcolor})
        
        
        N2eq10=TexMobject("\int^","{v}","_{v_0}{d ","{v}","\\over ","{v}"," } = -\\frac{c}{m} \int_{0}^{t} dt")        
        N2eq10.next_to(N2eq9,DOWN)
        N2eq10.set_color_by_tex_to_color_map({
            "{v}": speedcolor})
    
        
        N2eq11=TexMobject("\ln \\left({","{v}","\\over v_0}  \\right) = -{c\\over m}  t")    #{-v_t d ","{u}","\\over ","{u}"," }     
        N2eq11.next_to(N2eq9,DOWN)
        N2eq11.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":GREEN}) 
        
        N2eq12=TexMobject("{v}","(t)=v_0\\exp \\left( -{c\\over m}  t \\right) ")    #{-v_t d ","{u}","\\over ","{u}"," }     
        N2eq12.next_to(N2eq9,DOWN)
        N2eq12.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":GREEN}) 
        
        
    
        self.play(Write(solvetext), Write(N2eq8)) #N2 draws on screen
        self.wait(5) #"It says: How much the ball changes its speed depends on all the forces acting on it"
        self.play(Write(N2eq9))
        self.wait(5)# The Gravity and Drag on the ball are given by these expressions
        self.play(Write(N2eq10))
        self.wait(5)
        self.play(Transform(N2eq10,N2eq11))
        self.wait(5)
        self.play(Transform(N2eq10,N2eq12))
        self.wait(5)
        cleartext=TexMobject("   ")
        self.play(ApplyMethod(N2eq10.move_to,UP*2.25),Transform(N2eq9,cleartext),Transform(N2eq8,cleartext),Transform(solvetext,cleartext),Transform(N2eq3,cleartext),Transform(N2eq2,cleartext),Transform(N2eq1,cleartext),Transform(Headtext,cleartext))
        self.wait(2)
        
        Toptext=TextMobject("{Speed}"," decreases exponentially.")
        Toptext.to_edge(UP)
        Toptext.set_color_by_tex_to_color_map({"{Speed}": BLUE}) 
        
        self.play(Write(Toptext))
        self.wait(3)
        chartext=TextMobject("Characteristic time:")
        chartext.move_to(DOWN)
        tautext=TexMobject("\\tau = {m \\over c}")
        tautext.next_to(chartext,DOWN)
        
        self.play(Write(chartext))
        self.play(Write(tautext))
        
        N2eq13=TexMobject("{v}","(t)=v_0\\exp \\left( -{t\\over \\tau}   \\right) ")    #{-v_t d ","{u}","\\over ","{u}"," }     
        N2eq13.move_to(2.25*UP)
        N2eq13.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":GREEN}) 
        
        self.play(Transform(N2eq10,N2eq13))
        self.wait(3)
        
        questiontext=TextMobject("Let's graph it!")
        questiontext.move_to(UP*0.5)
        box = Rectangle(height=0.75, width=5,fill_color=BLACK, fill_opacity=1, color=GOLD_A)
        box.move_to(UP*0.5)
        self.play(ShowCreation(box),Write(questiontext),run_time=3)
                
        
        self.wait(3)


        #Text1.shift(RIGHT)
        #self.wait()
        
        
class VGraph(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 6,
        "y_min" : 0,
        "y_max" : 1.3,
        "graph_origin" : DL*3+2*LEFT ,
        "function_color" : RED ,
        "axes_color" : GOLD_E,
        "y_tick_frequency" : 0.1 ,
        "y_labeled_nums" : range(0,2),
        "y_label_decimal":3,
        "y_axis_label": "${v \\over v_0}$",
        "y_label_direction":2*LEFT,
        "exclude_zero_label": True,


        "x_labeled_nums" :range(0,7,1),        
        "x_axis_label": "${t\\over\\tau}$",
        "x_label_direction":DOWN ,
        
                        

    }   

    def construct(self):
        ### Set up the graph ###
        self.setup_axes(animate=True)
        
        N2eq13=TexMobject("{v}","(t)=v_0\\exp \\left( -{t\\over \\tau}   \\right) ")    #{-v_t d ","{u}","\\over ","{u}"," }     
        N2eq13.move_to(3.25*UP)
        N2eq13.set_color_by_tex_to_color_map({"{v}": BLUE, "{u}":GREEN}) 
    
        tautext=TexMobject("\\tau = {m \\over c}")
        tautext.next_to(N2eq13,DOWN)
        
    
        self.play(Write(N2eq13),Write(tautext))
    
        func_graph=self.get_graph(self.vfunc,color=BLUE)
        graph_lab = self.get_graph_label(func_graph,label="v(t)" )
        self.play(ShowCreation(func_graph),Write(graph_lab))
        self.wait(5)
        
        bigmsmallc=TextMobject("Small m or big c:")
        bigmsmallc.set_color_by_tex_to_color_map({"Small m or big c:": RED})
        bigmsmallc.next_to(tautext,DOWN)
        
        cartext1=TextMobject("Car slows down fast!")
        cartext1.set_color_by_tex_to_color_map({"Car slows down fast!": RED})
        cartext1.next_to(tautext,DOWN)
        
        self.play(Write(bigmsmallc))
        self.wait(3)
        func_graph2=self.get_graph(self.vfunc2,color=RED)
        self.play(ShowCreation(func_graph2))
        self.wait(3)
        self.play(Transform(bigmsmallc,cartext1))
        self.wait(5)
        
        
        smallmsbigc=TextMobject("Big m or small c:")
        smallmsbigc.set_color_by_tex_to_color_map({"Big m or small c:": GREEN})
        smallmsbigc.next_to(tautext,DOWN)

        cartext2=TextMobject("Car stays in motion longer!")
        cartext2.set_color_by_tex_to_color_map({"Car stays in motion longer!": GREEN})
        cartext2.next_to(tautext,DOWN)


        self.play(Transform(bigmsmallc,smallmsbigc))
        self.wait(3)
        func_graph3=self.get_graph(self.vfunc3,color=GREEN)
        self.play(ShowCreation(func_graph3))
        self.play(Transform(bigmsmallc,cartext2))
        self.wait(5)
        
        questiontext=TextMobject("Thanks for watching!")
        #questiontext.move_to(UP*0.5)
        box = Rectangle(height=0.75, width=7,fill_color=BLACK, fill_opacity=1, color=GOLD_A)
        #box.move_to(UP*0.5)
        self.play(ShowCreation(box),Write(questiontext),run_time=3)
        self.wait(5)
        
    
    def vfunc(self,t):
        return np.exp(-t)
    def vfunc2(self,t):
        return np.exp(-t/0.2)
    def vfunc3(self,t):
        return np.exp(-t/5)
    
            
