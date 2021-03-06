# ----------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------
import pymel.core as pm

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------



# ----------------------------------------------------------------------
# Main Script
# ----------------------------------------------------------------------
lis_sel = pm.ls(sl=True)

if lis_sel:
    for sel in lis_sel:
        print(sel)
        if pm.nodeType(sel) == "VRayObjectProperties":
            render_layer = pm.editRenderLayerGlobals(query=True, currentRenderLayer=True)
            try:
                print(render_layer)
                pm.editRenderLayerAdjustment(sel.ignore, layer=render_layer)
                pm.editRenderLayerAdjustment(sel.primaryVisibility, layer=render_layer)
                pm.setAttr(sel.ignore, 0)
                pm.setAttr(sel.primaryVisibility, 0)
            except Exception as ex:
                print('ERROR: {}'.format(ex))