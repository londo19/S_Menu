import bpy, os  
from bpy.props import EnumProperty, BoolProperty, IntProperty
from . ui.pie_menus import (
    SM_PIE_Add_Call,
    SM_PIE_Add_Node_Call, 
    SM_PIE_Q_Menu_Call, 
    SM_PIE_A_OM_Call, 
    SM_PIE_Q_Node_Call,
    SM_PIE_A_NODE_Call,
    SM_PIE_Tab_Menu_Call,
    SM_PIE_M4_Menu_Call,
)
# todo create enable all options function for each menu

# -----------------------------------------------------------------------------
#    Keymap      
# -----------------------------------------------------------------------------

addon_keymaps = []

def add_hotkey():
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if not kc:
        print('Keymap Error')
        return
    # object Mode
    km = kc.keymaps.new(name='Object Mode', space_type='EMPTY')

    kmi = km.keymap_items.new(SM_PIE_Add_Call.bl_idname, 'A', 'PRESS', ctrl=False, shift=True)
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new(SM_PIE_Q_Menu_Call.bl_idname, 'Q', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new(SM_PIE_A_OM_Call.bl_idname, 'A', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
    # object Mode
    km = kc.keymaps.new(name='Object Non-modal')
    
    kmi = km.keymap_items.new(SM_PIE_Tab_Menu_Call.bl_idname, 'TAB', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new(SM_PIE_M4_Menu_Call.bl_idname, 'BUTTON4MOUSE', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
    # edit mode (Mesh)
    km = kc.keymaps.new(name='Mesh')
    
    # node edtitors (comp/shader/texture)
    km = kc.keymaps.new(name='Node Generic', space_type='NODE_EDITOR')

    kmi = km.keymap_items.new(SM_PIE_Add_Node_Call.bl_idname, 'A', 'PRESS', ctrl=False, shift=True)
    addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new(SM_PIE_Q_Node_Call.bl_idname, 'Q', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new(SM_PIE_A_NODE_Call.bl_idname, 'A', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
   
def remove_hotkey():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()

# -----------------------------------------------------------------------------
#    Preferences      
# ----------------------------------------------------------------------------- 

def get_addon_name():
    return os.path.basename(os.path.dirname(os.path.realpath(__file__)))

def get_prefs():
    return bpy.context.preferences.addons[get_addon_name()].preferences


# Preferences            
class SM_Prefs(bpy.types.AddonPreferences):
    bl_idname = get_addon_name()
    
    tabs = [
        ("LIST", "Menu List", ""),
        #("ADD", "Add", ""),
        #("QMENU", "Q Menu", ""),
        ("OPTIONS", "Options", ""),
        #("UTILS", "Utils", ""),
    ]
    add_sub_tabs = [
        ("OBJECT", "Object Add Menu", ""),
        ("NODE", "Node Add Menu", ""),
    ]
    options_sub_tabs = [
        ("MAIN", "Main", ""),
        ("ADD", "Add", ""),
        ("QMENU", "Q Menu", ""),
        ("UTILS", "Utils", ""),
    ]
    q_sub_tabs = [
        ("OBJECT", "Object Mode Menu", ""),
        ("NODE", "Node Menu", ""),
    ]
    

    #§ Tab Props
    main_tabs: EnumProperty(name="Main_Tab", items=tabs)
    add_sub_tabs: EnumProperty(name="Add_Sub_Tab", items=add_sub_tabs)
    q_sub_tabs: EnumProperty(name="Q_sub_Tab", items=q_sub_tabs)
    options_sub_tabs: EnumProperty(name="Options_sub_Tab", items=options_sub_tabs)

    #§ Enable Props
    enable_qblocker: BoolProperty(
        name="QBlocker",
        default=True
    )
    enable_bolt: BoolProperty(
        name="Bolt",
        default=True
    )
    enable_landscape: BoolProperty(
        name="A.N.T. Landscape",
        default=True
    )
    enable_rock: BoolProperty(
        name="Rock Generator",
        default=True
    )
    enable_pipenightmare: BoolProperty(
        name="Pipe Nightmare",
        default=True
    )
    enable_extra_objects_mesh: BoolProperty(
        name="Extra Objects (Mesh)",
        default=True
    )
    enable_hops: BoolProperty(
        name="Hard Ops",
        default=True
    )
    enable_rarray: BoolProperty(
        name="R.Array",
        default=True
    )
    enable_box_cutter: BoolProperty(
        name="Box Cutter",
        default=True
    )
    enable_pose_buttons: BoolProperty(
        name="Pose Buttons",
        default=True
    )
    enable_images_as_planes: BoolProperty(
        name="Images as Planes",
        default=True
    )
    enable_camera_rigs: BoolProperty(
        name="Add Camera Rigs",
        default=True
    )
    #§ UI Pie Menu Radius
    SM_PIE_Radius: IntProperty(name="      ", default=120, min=0)
    #§ UI Bool Props
    collapse_list_options: BoolProperty(name="Options", default=False)
    collapse_list_menus: BoolProperty(name="Menus", default=False)
    collapse_list_view3d: BoolProperty(name="View 3D:", default=False)
    collapse_list_object_mode: BoolProperty(name="Object Mode:", default=False)
    collapse_list_node: BoolProperty(name="Nodes:", default=False)
    #§ comp_adjust_view Prefs
    SM_Modal_adjust_view_suppress_move: BoolProperty(default=False)
    #§ SM_MH Prefs
    show_delete_instances: BoolProperty(name="Delete All Instances", default=False)
    sm_mh_del_inst = [
        ("NO", "No", ""),
        ("YES", "Yes", ""),
    ]
    sm_mh_del_inst: EnumProperty(name="Q_sub_Tab", items=sm_mh_del_inst)
    ''' later ? , IntProperty
    SM_MH_auto_instance_inerval: IntProperty(
        name="Auto Instance Interval", 
        default=2,
        min=2,
        description="Auto Instance Interval (In seconds)"
    )'''

    def add_keymap_to_ui(self, context, layout, k_name, idname):
        # keymap_item = context.window_manager.keyconfigs.addon.keymaps[k_name].keymap_items
        keymap_item = context.window_manager.keyconfigs.user.keymaps[k_name].keymap_items
        row = layout.row()
        km = context.window_manager.keyconfigs.user.keymaps[k_name]  # added
        layout.context_pointer_set("keymap", km)  # added
        row.prop(keymap_item[idname], 'active', text="",full_event=True)
        row.prop(keymap_item[idname], 'type', text=keymap_item[idname].name, full_event=True) 


    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        row = col.row()
        row.prop(self, "main_tabs", expand=True)
  
        
        if self.main_tabs == "LIST":
            self.List_tab(context, col)
        #if self.main_tabs == "ADD":
        #    box = col.box()
        #    self.add_main_tab(context, box)
        #if self.main_tabs == "QMENU":
        #    box = col.box()
        #    self.q_main_tab(context, box)
        if self.main_tabs == "OPTIONS":
            box = col.box()
            self.Options_tab(context, box)
        #if self.main_tabs == "UTILS":
        #    box = col.box()
        #    self.utils_main_tab(context, box)
            
    def List_tab(self, context, col):
        
        sub = col.box()
        
        if self.collapse_list_menus is True:
            icon = "TRIA_RIGHT"
        else:
            icon = "TRIA_DOWN"
        sub.prop(self,"collapse_list_menus", icon=icon)
        
        if self.collapse_list_menus is False:
            sub = sub.box()
            
            if self.collapse_list_object_mode is True:
                icon = "TRIA_RIGHT"
            else:
                icon = "TRIA_DOWN"
            sub.prop(self,"collapse_list_object_mode", icon=icon)
            if self.collapse_list_object_mode is False:
                self.add_keymap_to_ui(context, sub, 'Object Mode', SM_PIE_Add_Call.bl_idname)
                self.add_keymap_to_ui(context, sub, 'Object Mode', SM_PIE_A_OM_Call.bl_idname)
                self.add_keymap_to_ui(context, sub, 'Object Mode', SM_PIE_Q_Menu_Call.bl_idname)
            
            if self.collapse_list_view3d is True:
                icon = "TRIA_RIGHT"
            else:
                icon = "TRIA_DOWN"
            sub.prop(self,"collapse_list_view3d", icon=icon)
            if self.collapse_list_view3d is False:
                self.add_keymap_to_ui(context, sub, 'Object Non-modal', SM_PIE_Tab_Menu_Call.bl_idname)
                self.add_keymap_to_ui(context, sub, 'Object Non-modal', SM_PIE_M4_Menu_Call.bl_idname)

            if self.collapse_list_node is True:
                icon = "TRIA_RIGHT"
            else:
                icon = "TRIA_DOWN"
            sub.prop(self,"collapse_list_node", icon=icon)
            if self.collapse_list_node is False:
                self.add_keymap_to_ui(context, sub, 'Node Generic', SM_PIE_Add_Node_Call.bl_idname)
                self.add_keymap_to_ui(context, sub, 'Node Generic', SM_PIE_Q_Node_Call.bl_idname)
                self.add_keymap_to_ui(context, sub, 'Node Generic', SM_PIE_A_NODE_Call.bl_idname)
  
    def Options_tab(self, context, col):
        
        row = col.row()
        row.prop(self, "options_sub_tabs", expand=True)


        if self.options_sub_tabs == "MAIN":
            self.Options_sub_tab_main(context, col)
        
        if self.options_sub_tabs == "ADD":
            self.add_main_tab(context, col)
       
        if self.options_sub_tabs == "QMENU":
            self.q_main_tab(context, col)
       
        if self.options_sub_tabs == "UTILS":
            self.utils_main_tab(context, col)

    def Options_sub_tab_main(self, context, col):
       
        sub = col.box()
        if self.collapse_list_options is True:
            icon = "TRIA_RIGHT"
        else:
            icon = "TRIA_DOWN"
        sub.prop(self,"collapse_list_options", icon=icon)
        if self.collapse_list_options is False:
            row = sub.row()
            row.use_property_split = True
            row.label(text="Pie Menu Radius WIP")
            row.prop(self, "SM_PIE_Radius", icon='PROP_CON')

   
    def add_main_tab(self, context, col):
        
        row = col.row()
        row.prop(self, "add_sub_tabs", expand=True)
        
        if self.add_sub_tabs == "OBJECT":
            self.add_sub_object(context, col)
        elif self.add_sub_tabs == "NODE":
            self.add_sub_node(context, col)
    
    def q_main_tab(self, context, col):
        
        row = col.row()
        row.prop(self, "q_sub_tabs", expand=True)
        
        if self.q_sub_tabs == "OBJECT":
            self.q_sub_object(context, col)
        elif self.q_sub_tabs == "NODE":
            self.q_sub_node(context, col)

    def utils_main_tab(self, context, col):
        
        col.label(text="Options:")
        col.prop(self, "enable_pose_buttons", text="Enable Copy/Paste Buttons In Header")
        col.label(text="Keymaps:")
        self.add_keymap_to_ui(context, col, 'Object Mode', SM_PIE_A_OM_Call.bl_idname)
        self.add_keymap_to_ui(context, col, 'Node Generic', SM_PIE_A_NODE_Call.bl_idname)
        self.add_keymap_to_ui(context, col, 'Object Non-modal', SM_PIE_Tab_Menu_Call.bl_idname)
        self.add_keymap_to_ui(context, col, 'Object Non-modal', SM_PIE_M4_Menu_Call.bl_idname)
        

    def add_sub_object(self, context ,col):
        col.label(text="Options:")
        col.label(text="Please Disable if not installed")
        col.prop(self, "enable_qblocker", text="QBlocker")
        col.prop(self, "enable_bolt", text="Bolt Factory")
        col.prop(self, "enable_landscape", text="A.N.T. Landscape")
        col.prop(self, "enable_rock", text="Rock Generator")
        col.prop(self, "enable_pipenightmare", text="Pipe Nightmare")
        col.prop(self, "enable_extra_objects_mesh", text="Extra Objects (Mesh)")
        col.prop(self, "enable_images_as_planes", text="Import Images as Planes")
        col.prop(self, "enable_camera_rigs", text="Add Camera Rigs")

        col.label(text="Keymap:")
        self.add_keymap_to_ui(context, col, 'Object Mode', SM_PIE_Add_Call.bl_idname)
     
    def add_sub_node(self, context ,col):
        col.label(text="Keymap:")
        
        self.add_keymap_to_ui(context, col, 'Node Generic', SM_PIE_Add_Node_Call.bl_idname)

    def q_sub_object(self, context, col):
        col.label(text="Options:")
        col.label(text="Please Disable if not installed")
        col.prop(self, "enable_hops", text="Hard Ops")
        col.prop(self, "enable_rarray", text="R.Array")
        col.prop(self, "enable_box_cutter", text="Box Cutter")
        col.label(text="Keymap:")

        self.add_keymap_to_ui(context, col, 'Object Mode', SM_PIE_Q_Menu_Call.bl_idname)

    def q_sub_node(self, context, col):
        col.label(text="Options:")
        col.label(text="Keymap:")
        self.add_keymap_to_ui(context, col, 'Node Generic', SM_PIE_Q_Node_Call.bl_idname)
