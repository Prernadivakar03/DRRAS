import * as React from "react";
import { cn } from "@/lib/utils";

const Card = React.forwardRef(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("rounded-lg border bg-white p-4 shadow", className)} {...props} />
));
Card.displayName = "Card";

const CardHeader = ({ className, ...props }) => (
  <div className={cn("border-b pb-2", className)} {...props} />
);

const CardContent = ({ className, ...props }) => (
  <div className={cn("py-2", className)} {...props} />
);

const CardFooter = ({ className, ...props }) => (
  <div className={cn("border-t pt-2", className)} {...props} />
);

export { Card, CardHeader, CardContent, CardFooter };
