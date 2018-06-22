from plotly.basedatatypes import BaseTraceHierarchyType


class Decreasing(BaseTraceHierarchyType):

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.ohlc.decreasing.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the line color.
                dash
                    Sets the dash style of lines. Set to a dash
                    type string (*solid*, *dot*, *dash*,
                    *longdash*, *dashdot*, or *longdashdot*) or a
                    dash length list in px (eg *5px,10px,2px,2px*).
                width
                    Sets the line width (in px).

        Returns
        -------
        plotly.graph_objs.ohlc.decreasing.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'ohlc'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        line
            plotly.graph_objs.ohlc.decreasing.Line instance or dict
            with compatible properties
        """

    def __init__(self, line=None, **kwargs):
        """
        Construct a new Decreasing object
        
        Parameters
        ----------
        line
            plotly.graph_objs.ohlc.decreasing.Line instance or dict
            with compatible properties

        Returns
        -------
        Decreasing
        """
        super(Decreasing, self).__init__('decreasing')

        # Import validators
        # -----------------
        from plotly.validators.ohlc import (decreasing as v_decreasing)

        # Initialize validators
        # ---------------------
        self._validators['line'] = v_decreasing.LineValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.line = line

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)