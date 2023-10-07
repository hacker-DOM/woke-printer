from __future__ import annotations

import networkx as nx
import rich_click as click
import woke.ir as ir
import woke.ir.types as types
from rich import print
from woke.printers import Printer, printer


class CfgStoragePrinter(Printer):
    def print(self) -> None:
        pass

    def visit_variable_declaration(self, node: ir.VariableDeclaration):
        from rich.syntax import Syntax

        if not node.is_state_variable:
            return
        for ref in node.references:
            if isinstance(ref, (ir.Identifier, ir.MemberAccess)):
                statement = ref.statement
                func_or_mod = statement.declaration
                cfg = func_or_mod.cfg
                cfg_block = cfg.get_cfg_block(statement)

                print(f"State variable [bold]{node.name}[/bold] used in {func_or_mod.canonical_name}:")
                print(Syntax(statement.source, "solidity"))
                print("")

    @printer.command(name="cfg-storage")
    def cli(self) -> None:
        pass